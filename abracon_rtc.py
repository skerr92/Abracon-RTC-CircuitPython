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

ADDRESS = (0x68)

# TODO: add register macros
# Registers 0x00 - 0x0F


class ABRA_RTC:

    def __init__(self, i2c, address=ADDRESS):
      self._i2c = i2c_device.I2CDevice(i2c, address)
      self._buffer = bytearray(2)
      self.reset()

    def get_seconds():
        with self._i2c as dev:
            res = bytearray(1)
            dev.write_then_readinto(bytes([0x01]), self._buffer, in_end=1)
            return int(res[0])

    def get_minute():
        with self._i2c as dev:
            dev.write_then_readinto(bytes([0x02]), self._buffer, in_end=1)
            return int(res[0])

    def get_hour():
        with self._i2c as dev:
            dev.write_then_readinto(bytes([0x03]), self._buffer, in_end=1)
            return int(res[0])

    def set_freq_comp(val):
        with self._i2c as dev:
            dev.write(bytes([0x08,val]))

    def set_seconds(secs):
        with self._i2c as dev:
            dev.write(bytes([0x01,secs]))
            dev.write_then_readinto(bytes([0x01]), self._buffer, in_end=1)
            #print("seconds: ", res[0])

    def set_minute(min):
        with self._i2c as dev:
            int(min)
            dev.write(bytes([0x02,min]))
            dev.write_then_readinto(bytes([0x02]), self._buffer, in_end=1)
            #print("minutes: ", res[0])

    def set_hour(hr):
        with self._i2c as dev:
            dev.write(bytes([0x03,hr]))
            dev.write_then_readinto(bytes([0x03]), self._buffer, in_end=1)
            #print("hours: ", res[0])
