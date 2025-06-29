# SmartClockPi

A Raspberry Pi Zero 2 W based smart clock with touchscreen display, environmental sensing, and internet weather integration.

## KiCad Stuff

This project uses KiCad for PCB design. The files are located in the `PCB/` directory. You can open them with KiCad to view the schematics and PCB layout. These are the screenshots of the PCB and schematics:

### PCB Design

<img width="750" alt="PCB image" src="assets/pcb_image.png" />

### Schematics

<img width="750" alt="Schematics image" src="assets/schematics_image.png" />

## Sketch

<img width="750" alt="sketch" src="https://github.com/user-attachments/assets/283bab9a-2045-44e5-bac4-4e4c9ae9bedf" />

## Why I Made This

I wanted a smart clock that could display the time, date, indoor temperature, humidity, and outdoor weather conditions. I also wanted it to have a touchscreen interface for easy interaction. The Raspberry Pi Zero 2 W was chosen for its compact size and sufficient processing power for this project.

"Why don't you just buy a pre-made smart clock?" you might ask. Well, I wanted to learn more about PCB layout/designing. This project is a great way to "exercise" while creating something useful for myself.

Also, I wanted to make it modular so I can easily swap out components or add new features in the future. The custom PCB design allows for easy connections and modifications.

## Features

### Display & Interface

- **3.5" ILI9488 SPI TFT Touchscreen** (480x320 pixels)
- Resistive touch input for UI
- Large, clear font display for time and date
- Automatic brightness adjustment via photoresistor (TO-DO, once I get the parts)

### Environmental Monitoring

- **DHT22 Sensor** for indoor temperature, humidity readings
- Real-time sensor data updates

### Weather Integration

- Internet weather data from wttr.in (Auckland, Half Moon Bay area)
- No API key required
- Displays outdoor temperature, humidity, and weather status
- Update every 10 minutes

### Time & Clock Features

- **DS3231 Real-Time Clock (RTC)** with battery backup
- Maintains accurate time even when Pi is powered off (or when my internet dies)
- Large, readable time display

### Hardware Features

- Custom PCB design with modular connections (so i can unplug and replug the modules)
- Female header pins for easy module connection
- Compact form factor (94.5mm x 67.2mm PCB)

## Hardware Components

Please see [SmartClockPi-bom.csv](SmartClockPi-bom.csv) (Created since this is required for Highway)

## Software Features

- **Python-based application** using:
  - `luma.lcd` for display control
  - `adafruit-circuitpython-bme280` for sensor interface
  - `Pillow` for graphics rendering
- Real-time clock display with large, clear fonts. Need to test if this actually works
- Weather data integration from wttr.in
- Environmental sensor monitoring

## Project Structure

```txt
SmartClockPi/
├── README.md
├── JOURNAL.md                # Development journal with progress updates
├── SmartClockPi-bom.csv      # Bill of Materials
├── PCB/                      # KiCad PCB design files
│   ├── smartclockpi.kicad_pro
│   ├── smartclockpi.kicad_sch
│   ├── smartclockpi.kicad_pcb
│   └── Gerber/               # Manufacturing files
└── [Software files to be added]
```

## License

This project is Free and Open-source, licensed under the GPLv3 license. Feel free to contribute or use it for your own projects!

See [LICENSE](LICENSE) for more details.

---
