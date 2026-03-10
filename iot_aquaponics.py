import time
import board
import busio
import RPi.GPIO as GPIO
import minimalmodbus
import serial
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from pymodbus.client import ModbusSerialClient
from RPLCD.i2c import CharLCD
RELAY1_PIN = 17   
RELAY2_PIN = 27   
AERATION_PIN = 22 

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY1_PIN, GPIO.OUT)
GPIO.setup(RELAY2_PIN, GPIO.OUT)
GPIO.setup(AERATION_PIN, GPIO.OUT)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
soil_channel = AnalogIn(ads, ADS.P0)
client = ModbusSerialClient(
    method='rtu',
    port='/dev/ttyUSB0',  
    baudrate=9600,
    timeout=1
)
lcd = CharLCD('PCF8574', 0x27) 
def read_soil_moisture():
    return soil_channel.value

def read_npk():
    if client.connect():
        result = client.read_holding_registers(1, 3, unit=1)
        client.close()
        if not result.isError():
            nitrogen, phosphorus, potassium = result.registers
            return nitrogen, phosphorus, potassium
    return None, None, None

def control_pump(relay_pin, state):
    GPIO.output(relay_pin, GPIO.HIGH if state else GPIO.LOW)

def update_display(n, p, k, moisture):
    lcd.clear()
    lcd.write_string(f"N:{n} P:{p} K:{k}\nMoist:{moisture}")
try:
    while True:
        moisture = read_soil_moisture()
        n, p, k = read_npk()
        print(f"Soil Moisture: {moisture}")
        print(f"N:{n} P:{p} K:{k}")
        if moisture < 10000:  
            control_pump(RELAY2_PIN, True)
        else:
            control_pump(RELAY2_PIN, False)
        update_display(n, p, k, moisture)

        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()