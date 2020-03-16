'''
Documentation:
https://circuitpython.readthedocs.io/projects/pca9685/en/latest/api.html
@author: matt
'''

import board
import busio
import adafruit_pca9685
#from adafruit_blinka.microcontroller.ft232h import i2c

i2c = busio.I2C(board.SCL, board.SDA)
servoHat = adafruit_pca9685.PCA9685(i2c)

servoHat.frequency = 50 # in Hz

servoChannel = servoHat.channels[0]
servoChannel.duty_cycle = 1999 # 10% duty cycle (0x000 -> 0xffff) - hex

'''
If controlling servos that are continuous, or that hold angles, the servo library may prove 
more usefull:
https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/using-the-python-library
'''
                     