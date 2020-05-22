#!/usr/bin/env python3
# An EV3 Python (library v2) solution to Exercise 3
# of the official Lego Robot Educator lessons that
# are part of the EV3 education software
import ev3dev2
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from time import sleep
from ev3dev2.motor import SpeedNativeUnits
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
tank_pair.on(left_speed=0, right_speed=0)
