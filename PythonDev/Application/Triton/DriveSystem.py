'''
Created on Feb 4, 2020

@author: matt
'''

import board
import busio
import adafruit_pca9685
import time

class DriveSystem(object):
    '''
    classdocs
    '''
    VICTOR_FREQ = 50                # Hz, freq of base signal
    VICTOR_DUTY_MIN = 0x0ccd        # 5% of 0xffff in hex
    VICTOR_DUTY_MAX = 0x1999        # 10% of 0xffff in hex
    VICTOR_DUTY_NEUTRAL = 0x1333    # 7.5% of 0xffff in hex

    def __init__(self, motorRightPort = 1, motorLeftPort = 2, i2c = None):
        '''
        Constructor
        '''
        if i2c is None:
            try:
                i2c = busio.I2C(board.SCL, board.SCA)
            except(AttributeError):
                print("Are you trying to run on windows?  DriveSystem will not work due to the board import")
                self.pwmHatConnected = False
                return
        self.setupPwmHat(i2c, motorRightPort, motorLeftPort)
        

    def RawInput(self, r_motor, l_motor):
  
    def setupPwmHat(self, i2c, rightPort, leftPort):
        global VICTOR_FREQ
        self.pwmHat = adafruit_pca9685.PCA9685(i2c)
        self.pwmHatConnected = True
        self.pwmHat.frequency = VICTOR_FREQ
        self.motorRightChannel = self.pwmHat.channels[rightPort]
        self.motorLeftChannel = self.pwmHat.channels[leftPort]

    def turnBot(self, angleRad, speed):
        ''' 
        Turns the Robot relative to the angleRad, changing the set speed to speed
        
        @param angleRad describes desired turn, pos is CCW
        @param speed    describes set speed of motors in m/s
        @return state of execution
        ''' 
        return False
    
    def changeSpeed(self, speed):
        '''
        Changes overall speed set of bot
        
        @param speed describes set speed of motors in m/s
        @return state of execution
        '''
        
    def testFireVictor(self, motorChannel, seconds):
        '''
        Testing method that fires right motor for ___ time
        @return state of execution
        '''
        if not self.pwmHatConnected:
            self.printNoHatConnected()
            return

        global VICTOR_DUTY_MAX, VICTOR_DUTY_NEUTRAL

        motorChannel.duty_cycle = VICTOR_DUTY_MAX
        time.sleep(seconds)
        motorChannel.duty_cycle = VICTOR_DUTY_NEUTRAL
        

    def fireRightMotor(self,seconds = 1):
        '''
        Testing method that fires right motor for ___ time
        @return state of execution
        '''
        if not self.pwmHatConnected:
            self.printNoHatConnected()
            return

        self.testFireVictor(self.motorRightChannel, seconds)

    def fireLeftMotor(self, seconds = 1):
        '''
        Testing method that fires right motor for ___ time
        @return state of execution
        '''
        if not self.pwmHatConnected:
            self.printNoHatConnected()
            return 

        self.testFireVictor(self.motorLeftChannel, seconds)

    def goStraight(self, doubleHere, doubleThere):
        if not self.pwmHatConnected:
            self.printNoHatConnected()
            return

        self.FireLeftMotor(doubleHere)
        self.FireRightMotor(doubleThere)

    @staticmethod
    def printNoHatConnected():
        print("Cannot control motors without PWM hat connected")
    
        
