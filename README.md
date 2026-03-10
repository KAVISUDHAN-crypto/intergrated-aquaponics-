# INTERGRATED AQUAPONICS  NUTRITION ND IoT MONITORING SYSTEM

This project implements a **iot based aquaponics** using Raspberry Pi (or ESP32) with multiple sensors and actuators. 
It monitors soil moisture, NPK nutrient levels, and water level, then controls pumps and aeration automatically. 
The system also displays real-time values on an LCD/OLED screen.
##  Block Diagram
- **Inputs:**
  - Soil Moisture Sensor (via ADS1115 ADC)
  - NPK Sensor (RS485 Modbus RTU)
  - Water Level Sensor (digital/analog)
- **Outputs:**
  - LCD/OLED Display (I²C)
  - Relay 1 → Water Pump 1 (fish tank → storage tank)
  - Relay 2 → Water Pump 2 (storage tank → soil)
  - Aeration Pump (storage tank)
##  Hardware Requirements
- Raspberry Pi (any model with GPIO/USB)
- ADS1115 ADC module
- Capacitive soil moisture sensor
- RS485 NPK sensor + USB-RS485 converter (or MAX485 module)
- Water level sensor
- Relays + pumps
- LCD (I²C 16x2/20x4) or OLED (SSD1306)
- Jumper wires, breadboard
**Usage**
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
