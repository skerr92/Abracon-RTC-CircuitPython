# Abracon RTCMC 32.768kHz Real Time Clock driver.
# Author: Seth Kerr
# License: MIT License (https://opensource.org/licenses/MIT)

"""
`abracon_rtc.py`
====================================================
CircuitPython driver for the Abracon RTCMC 32.768kHz Real Time Clock.
See usage in the examples/simpletest.py file.
* Author(s): Seth Kerr
Implementation Notes
--------------------
**Hardware:**
* Abracon RTCMC 32.768KHZ-AIGZ-S7 Real Time Clock - Abracon RTCMC
  <>`
**Software and Dependencies:**
* Adafruit CircuitPython firmware for the ESP8622 and M0-based boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
"""

import time

import adafruit_bus_device.i2c_device as i2c_device
from micropython import const

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/skerr92/abracon_rtc_circuitpython.git"

ADDRESS = (0x56)

# Registers 0x00 - 0x0F


class ABRA_RTC:

    def __init__(self, i2c, address=ADDRESS):
      self._i2c = i2c_device.I2CDevice(i2c, address)
      self._buffer = bytearray(2)
      self.reset()

    def _write_register_byte(self, register, value):


    def _read_register_byte(self, register, result, length=None):


    def reset(self):


    def set_time(self, time):


    def set_alarm(self, alarm):


    def set_watchdog(self, value):


    def get_second(self):


    def get_minute(self):


    def get_hour(self):


    def get_day(self):


    def get_month(self):


    def get_year(self):


    
