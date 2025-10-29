#A0 = SW420 Vibration Sensor

import machine
from machine import ADC
import utime

SW420 = machine.ADC(0)
#10bit ADC in ESP8266 0-1023 (0-5V )
while True:
    adc_value = SW420.read()
    print('SW420 ADC Value:',adc_value)
    utime.sleep_ms(200)