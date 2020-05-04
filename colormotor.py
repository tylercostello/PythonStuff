#!/usr/bin/env python3
# An EV3 Python (library v2) solution to Exercise 3
# of the official Lego Robot Educator lessons that
# are part of the EV3 education software
import ev3dev2
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from time import sleep
from ev3dev2.motor import SpeedNativeUnits

leftSpeeds=[]
rightSpeeds=[]
btn = Button() # we will use any button to stop script
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
leftMotor = ev3dev2.motor.Motor(OUTPUT_B)
rightMotor = ev3dev2.motor.Motor(OUTPUT_C)
# Connect an EV3 color sensor to any sensor port.
cl = ColorSensor()

while not btn.any():
    leftSpeeds=[]
    rightSpeeds=[]
    for x in range(600):
           # exit loop when any button pressed
        # if we are over the black line (weak reflection)
        if cl.reflected_light_intensity<30:
            # medium turn right

            leftMotor.on(SpeedNativeUnits(-100))
            #leftMotor.speedNativeUnits(-500)
            rightMotor.on(SpeedNativeUnits(0))

            #leftMotor.speedNativeUnits(-500)
            #rightMotor.speedNativeUnits(0)
            leftSpeeds.append(leftMotor.speed)
            rightSpeeds.append(rightMotor.speed)
            #tank_pair.on(left_speed=0, right_speed=-50)
            #print(leftMotor.speed)

        else:   # strong reflection (>=30) so over white surface
            # medium turn left
            leftMotor.on(SpeedNativeUnits(0))
            #leftMotor.speedNativeUnits(-500)
            rightMotor.on(SpeedNativeUnits(-100))
            #rightMotor.speedNativeUnits(-500)
            #leftMotor.speedNativeUnits(0)
            leftSpeeds.append(leftMotor.speed)
            rightSpeeds.append(rightMotor.speed)
            #tank_pair.on(left_speed=-50, right_speed=0)
            #print(leftMotor.speed)

        sleep(0.1) # wait for 0.1 seconds
    for y in range(len(leftSpeeds)):
        leftMotor.on(SpeedNativeUnits(-leftSpeeds[len(leftSpeeds)-y-1]))
        #leftMotor.speedNativeUnits(-500)
        rightMotor.on(SpeedNativeUnits(-rightSpeeds[len(rightSpeeds)-y-1]))
        #leftMotor.speedNativeUnits(leftSpeeds[len(leftSpeeds)-y])
        #rightMotor.speedNativeUnits(rightSpeeds[len(rightSpeeds)-y])
        sleep(0.1)

tank_pair.on(left_speed=0, right_speed=0)
