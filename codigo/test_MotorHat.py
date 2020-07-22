#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplo básico de movimiento de motores con Adafruit Motor Hat

https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi?view=all

CC by SA @javacasm
Julio 2020
"""

import time
from adafruit_motorkit import MotorKit
kit = MotorKit()

print('motor1')
kit.motor1.throttle = 1.0
time.sleep(5)
kit.motor1.throttle = 0

print('motor2')
kit.motor2.throttle = 1.0
time.sleep(5)
kit.motor2.throttle = 0

print('motor3')
kit.motor3.throttle = 1.0
time.sleep(5)
kit.motor3.throttle = 0

print('motor4')
kit.motor4.throttle = 1.0
time.sleep(5)
kit.motor4.throttle = 0