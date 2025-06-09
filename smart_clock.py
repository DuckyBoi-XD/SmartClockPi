import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from luma.core.interface.serial import spi
from luma.lcd.device import ili9488

# For BME280 sensor (temperature/humidity)
import board
import adafruit_bme280

# Initialise SPI display
serial = spi(port=0, device=0, gpio_DC=24, gpio_RST=25, bus_speed_hz=48000000)
device = ili9488(serial, width=480, height=320, rotate=0)

# Initialise BME280 sensor
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Fonts (use DejaVuSans or any TTF font you have)
font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 80)
font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

def get_weather_icon():
    """to-do: make this real"""
    # Simple dummy icon: sun
    icon = Image.new("RGBA", (80,80), (255,255,255,0))
    draw = ImageDraw.Draw(icon)
    draw.ellipse((10, 10, 70, 70), fill="yellow", outline="orange", width=4)
    return icon

while True:
    now = datetime.now()
    time_str = now.strftime("%H:%M")
    date_str = now.strftime("%a, %b %d")
    
    # Read BME280 sensor
    temperature = bme280.temperature
    humidity = bme280.humidity
    
    # Fake weather status
    """to-do: make this real"""
    weather_status = "Sunny"
    weather_icon = get_weather_icon()

    # Create blank canvas
    image = Image.new("RGB", (480, 320), "black")
    draw = ImageDraw.Draw(image)
    
    # Draw time
    draw.text((30, 30), time_str, font=font_large, fill="white")
    draw.text((35, 120), date_str, font=font_medium, fill="lightgray")
    
    # Draw temp/humidity
    temp_str = f"{temperature:.1f}°C"
    hum_str = f"{humidity:.0f}%"
    draw.text((350, 45), temp_str, font=font_medium, fill="orange")
    draw.text((350, 90), hum_str, font=font_medium, fill="skyblue")
    
    # Draw weather
    image.paste(weather_icon, (355, 150), weather_icon)
    draw.text((350, 240), weather_status, font=font_small, fill="yellow")
    
    # Draw a line separator
    draw.line([(0, 200), (480, 200)], fill="gray", width=2)
    
    # Display the image
    device.display(image)
    time.sleep(1)
