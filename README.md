# 💥 ESP8266 SW420 Vibration Sensor (ADC) — MicroPython

## 🧠 Overview
This project demonstrates how to read analog vibration data from an **SW420 vibration sensor** using the **ADC** pin on the **ESP8266** board.  
The analog output from the SW420 is connected to the **A0** pin and read continuously using **MicroPython**, printing the vibration level on the Thonny IDE console.

---

## ⚙️ Hardware Setup

| Component           | ESP8266 Pin | Description |
|---------------------|-------------|--------------|
| SW420 Vibration Sensor | A0       | Analog output pin |
| Power (VCC)         | 3.3V        | Sensor power supply |
| Ground (GND)        | GND         | Common ground |

🔹 The **SW420** sensor’s output voltage changes when vibration or shock is detected.  
🔹 Connect its **DO** pin to **A0** for analog voltage measurement.

---

## 🧩 Code

```python
# A0 = SW420 Vibration Sensor

import machine
from machine import ADC
import utime

SW420 = machine.ADC(0)
# 10-bit ADC in ESP8266: 0–1023 (0–1V input range)

while True:
    adc_value = SW420.read()
    print('SW420 ADC Value:', adc_value)
    utime.sleep_ms(200)
