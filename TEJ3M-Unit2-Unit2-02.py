#!/usr/bin/env python3

# Created by Samuel Webster
# Created on Feb 2023

import time
import board
from digitalio import DigitalInOut, Direction

# LED setup for onboard LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
blink_time = 1

while True:
    led.value = True
    time.sleep(blink_time)
    led.value = False
    time.sleep(1)

    blink_time += 1
