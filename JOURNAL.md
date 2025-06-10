---
title: "SmartClockPi"
author: "@QinCai-rui"
description: "A Raspberry Pi Zero 2 W based smart clock with touchscreen, environmental sensing, and more."
created_at: "2025-06-09"
---

## 8/6/25

### Update 1/1

Started a new project for a smart clock using the Raspberry Pi Zero 2 W.

**Planning:**
- Decided on a feature set: large touchscreen display, temperature/humidity/pressure monitoring, internet weather, touch sensing, and music playback for the alarm part.
- Researched and compared display modules -- settled on a [3.5" ILI9488 SPI TFT resistive touchscreen (480x320)](https://www.aliexpress.com/item/1005007096645415.html). Good size and clarity.
- Chose the [BME280 sensor](https://www.aliexpress.com/item/1005004527984343.html) for environmental data, using the I2C interface with the Pi and freeing SPI for the display.
- Support for both devices with available Python libraries (`luma.lcd`, `Pillow`, `adafruit-circuitpython-bme280`). (at least I hope so)

**Links:**  
- [3.5" ILI9488 SPI TFT Touch Display](https://www.aliexpress.com/item/1005007096645415.html)  
- [BME280 I2C/SPI Sensor Module](https://www.aliexpress.com/item/1005004527984343.html)

**Hardware & Wiring:**  
Used the pinout provided in the datasheet for the display:

<img width="400" alt="Screenshot 2025-06-09 at 7 57 09 AM" src="https://github.com/user-attachments/assets/7534f6dd-263e-4af9-aac8-a5d92e26f83b" />

The BME280: 

<img width="400" alt="Screenshot 2025-06-09 at 7 57 27 AM" src="https://github.com/user-attachments/assets/dabfdbd2-09e0-47c8-8cde-d9e1b7570a04" />


#### SPI Display Pins (ILI9488)
| Pin | Name      | Description                                    | Raspberry Pi Zero 2 W Pin   |
|-----|-----------|------------------------------------------------|-----------------------------|
| 1   | VCC       | 5V/3.3V power input                            | 3.3V (Pin 1 or 17)          |
| 2   | GND       | grounding                                      | GND (Pin 6 or 9)            |
| 3   | CS        | LCD chip select signal, low level enable       | GPIO8 (SPI0_CE0, Pin 24)    |
| 4   | RESET     | LCD reset signal, low level reset              | GPIO25 (Pin 22)             |
| 5   | DC/RS     | LCD register/data selection signal             | GPIO24 (Pin 18)             |
| 6   | SDI(MOSI) | SPI bus write data signal                      | GPIO10 (SPI0_MOSI, Pin 19)  |
| 7   | SCK       | SPI bus clock signal                           | GPIO11 (SPI0_SCLK, Pin 23)  |
| 8   | LED       | Backlight control (tie to 3.3V for always on)  | 3.3V (Pin 1 or 17)          |
| 9   | SDO(MISO) | SPI bus read data signal (optional)            | GPIO9 (SPI0_MISO, Pin 21)   |

#### Touch Panel Pins (if using touch, XPT2046 controller)
| Pin  | Name   | Description                              | Raspberry Pi GPIO (need to work this out later)   |
|------|--------|------------------------------------------|------------------------------|
| 10   | T_CLK  | Touch SPI bus clock signal               | Any free GPIO  |
| 11   | T_CS   | Touch chip select (active low)           | Any free GPIO    |
| 12   | T_DIN  | Touch SPI input                          | Any free GPIO         |
| 13   | T_DO   | Touch SPI output                         | Any free GPIO                |
| 14   | T_IRQ  | Touch interrupt (active low)             | Any free GPIO                |

#### BME280 Sensor (I2C)
| Pin  | Name | Description          | Raspberry Pi Zero 2 W Pin |
|------|------|----------------------|---------------------------|
| 1    | VCC  | 3.3V power           | 3.3V (Pin 1 or 17)        |
| 2    | GND  | Ground               | GND (Pin 6 or 9)          |
| 3    | SDA  | I2C data             | GPIO2 (I2C SDA, Pin 3)    |
| 4    | SCL  | I2C clock            | GPIO3 (I2C SCL, Pin 5)    |

- Both modules use 3.3V power (chose BME-3.3, so do NOT use 5V).
- LED pin on display can be tied to 3.3V for always-on backlight, or controlled by a PWM GPIO for dimming.

**TO_DO**
- add a photoresistor or something to chnage the bightness dynamically

Time spent today: **1.25 hours** (research, planning, reviewing libraries, looking for modules, and mapping out wiring)

---

## 10/6/25

### Update 1/2

Worked on SmartClockPi code and UI, even though I don't have the hardware yet.

**Today:**
- Wrote the main Python app logic for the clock display and sensor/weather integration.
- Used the `luma.lcd` library for the ILI9488 SPI display, and `adafruit-circuitpython-bme280` for the sensor interface.
- Integrated free weather data from wttr.in for Auckland, Half Moon Bay area (no API key required).
- The app will show:  
  - Real time and date (large, clear fonts)
  - Indoor temperature, humidity, and pressure (from BME280, once connected)
  - Outdoor weather: main status, temperature, humidity, and icon (from wttr.in)
- Weather auto-refreshes every 10 minutes, sensor data every second.
- Alarm logic is removed for now to keep the code simple.
- All code is structured to be ready for testing as soon as the display and sensors are available.
- Next steps: add touch UI, dynamic backlight (photoresistor), and maybe a settings menu.


Time spent today: **2 hours** (coding, planning UI, integrating wttr.in, and preparing for hardware)

