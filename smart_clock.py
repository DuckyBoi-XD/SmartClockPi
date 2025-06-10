import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from luma.core.interface.serial import spi
from luma.lcd.device import ili9488

import board
import adafruit_bme280
import requests



# --- INIT HARDWARE --
serial = spi(port=0, device=0, gpio_DC=24, gpio_RST=25, bus_speed_hz=48000000)
device = ili9488(serial, width=480, height=320, rotate=0)

i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 80)
font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# --- WEATHER (no API key) ---
def fetch_wttr_weather():
    try:
        # "Half Moon Bay, Auckland" - returns JSON
        url = "https://wttr.in/Half%20Moon%20Bay%20Auckland?format=j1"
        resp = requests.get(url, timeout=5)
        data = resp.json()
        current = data['current_condition'][0]
        weather = {
            "status": current['weatherDesc'][0]['value'],
            "temp_C": float(current['temp_C']),
            "humidity": int(current['humidity']),
            "icon_url": current.get('weatherIconUrl', [{}])[0].get('value', None)
        }
        return weather
    except Exception:
        return None

# --- Main UI loop ---
last_weather_refresh = 0
weather_data = None

def main():
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%a, %b %d %Y")

    # --- BME280 ---
    temperature = bme280.temperature
    humidity = bme280.humidity
    pressure = bme280.pressure

    # --- Weather fetch / 10 mins ---
    if time.time() - last_weather_refresh > 600 or not weather_data:
        wd = fetch_wttr_weather()
        if wd:
            weather_data = wd
        last_weather_refresh = time.time()

    # --- Weather icon ---
    weather_status = weather_data['status'] if weather_data else "No data"
    weather_temp = weather_data['temp_C'] if weather_data else None
    weather_hum = weather_data['humidity'] if weather_data else None
    weather_icon_url = weather_data['icon_url'] if weather_data else None

    # --- Draw UI ---
    image = Image.new("RGB", (480, 320), "black")
    draw = ImageDraw.Draw(image)

    # Draw time & date
    draw.text((30, 30), time_str, font=font_large, fill="white")
    draw.text((35, 120), date_str, font=font_medium, fill="lightgray")

    # Draw local BME280 temp/humidity/pressure
    temp_str = f"Indoor: {temperature:.1f}°C"
    hum_str = f"Humidity: {humidity:.0f}%"
    pres_str = f"Pressure: {pressure:.0f} hPa"
    draw.text((30, 180), temp_str, font=font_small, fill="orange")
    draw.text((30, 210), hum_str, font=font_small, fill="skyblue")
    draw.text((30, 240), pres_str, font=font_small, fill="yellow")

    # Draw weather (real, outdoor)
    draw.text((350, 30), "Wttr.in:", font=font_small, fill="white")
    if weather_icon_url:
        try:
            from io import BytesIO
            icon_resp = requests.get(weather_icon_url, timeout=3)
            icon_img = Image.open(BytesIO(icon_resp.content)).convert("RGBA").resize((64,64))
            image.paste(icon_img, (355, 60), icon_img)
        except Exception:
            pass
    draw.text((350, 130), f"{weather_status}", font=font_tiny, fill="yellow")
    if weather_temp is not None:
        draw.text((350, 150), f"{weather_temp:.1f}°C", font=font_small, fill="orange")
    if weather_hum is not None:
        draw.text((350, 180), f"{weather_hum:.0f}%", font=font_small, fill="skyblue")

    # Draw separator
    draw.line([(0, 270), (480, 270)], fill="gray", width=2)
    draw.text((10, 280), "Touch screen features coming soon | Ctrl+C to exit.", font=font_tiny, fill="gray")

    # Display the image
    device.display(image)

    time.sleep(1)

if __main__ == "main":
    while True:
        main()
