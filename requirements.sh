#!/bin/bash

# Create requirements.txt for iot based aquaponics
cat <<EOL > requirements.txt
adafruit-circuitpython-ads1x15==3.0.2
pymodbus==3.12.1
minimalmodbus==2.1.1
pyserial==3.5
RPi.GPIO==0.7.1
gpiozero==2.0.1
adafruit-circuitpython-charlcd==3.5.5
adafruit-circuitpython-ssd1306==2.12.22
paho-mqtt==2.1.0
requests==2.32.5
influxdb-client==1.50.0
EOL

echo "requirements.txt has been generated successfully!"
