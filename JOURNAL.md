---
title: "SmartClockPi"
author: "@QinCai-rui"
description: "A Raspberry Pi Zero 2 W based smart clock with touchscreen, environmental sensing, and more."
created_at: "2025-06-09"
---

## 8/6/25

### Update 1

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

#### Touch Panel Pins (using touch, XPT2046 controller)
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

Time spent today: **2 hours** (research, planning, reviewing libraries, looking for modules, and mapping out wiring)

---

## 10/6/25

### Update 2

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


Time spent this session: **1.5 hours**

---

### Update 3

I started working on the schematic for the project. I wanted to include both the Raspberry Pi header, the BME280 sensor, and the ILI9488 touchscreen display in my design. However, I ran into an issue: I couldn't find a suitable symbol or footprint for the LCD screen I’m using (the ILI9488 SPI TFT touchscreen) in my KiCad’s library. 

I decided to use generic header pins to represent the LCD screen in the schematic. This way, I was able to clearly show all of the required connections for the display, including the SPI and touch controller signals, power, and backlight control. 

<img width="250" alt="The LCD" src="https://github.com/user-attachments/assets/cbc5bc3f-4be9-495b-b5dd-a5738ce62850" />

When i get the PCB, I will just solder some female header pins (1x14) onto the board, and plug the screen in. I might need some standoffs though...

<img width="500" alt="Screenshot 2025-06-10 at 4 03 51 PM" src="https://github.com/user-attachments/assets/614353b9-a2c5-44db-b817-d876454f31ce" />

Next step: add in a photoresistor

Time spent this session: **3 hours**

---

## 11/6/25

### Update 4

I finalised my schematic during the session. The main challenge is to find the footprints and symbols for my parts. I ended up using female header pins to plug my modules in.

<img width="700" alt="Screenshot 2025-06-13 at 2 10 22 PM" src="https://github.com/user-attachments/assets/8b46b163-35c3-475e-a70f-2e2b0f7908da" />

Time spent this session: **5 hours**

---

## 12/6/25

### Update 5

Started working on the PCB. It was very stupid converting the schematics into PCB. The `Tools > Update PCB from schematics` was greyed out. But somehow I made it work after wasting a lot of time...

<img width="600" alt="Screenshot 2025-06-13 at 2 14 14 PM" src="https://github.com/user-attachments/assets/a3d68089-22b4-4e6e-8d0a-89676849072a" />

Time spent this session: **4 hours**

---

## 14/5/25 & 15/5/25

### Update 6



---

## 13/5/25 & 16/5/25

### Update 7

Did a lot of work on the PCB. I connected all my 17 parts (at the time of writing) together. The big, main issue I had was to get the blue "wires" (connector lines) to show up on some of the parts. Turned out KiCad didn't know which pins were which, so it ignored them. I changed the pin numbers from correct ones to lables, replacing the numbers, since I couldn't make the lables show up before. So I changed the pin numbers back, and YAY!!

![image](https://github.com/user-attachments/assets/8004084d-f2dd-41ae-8ae3-297c97ecfa25)
![image](https://github.com/user-attachments/assets/a15f812d-8b11-4a60-9d95-41e4d99620bc)

The PCB is done, so long as I don't decide to drop a few more parts in....

Time spent this session: **6 hours**
