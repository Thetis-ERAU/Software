'''
Created on Feb 4, 2020

@author: matt
'''
class DriveSystem(object):
    '''
    classdocs
    '''


    def __init__(self, lServoPort, rServoPort):
        '''
        Constructor
        '''
        self.leftWheelServo = lServoPort
        self.rightWheelServo = rServoPort
        
        
    def TurnBot(self, angleRad, speed):
        ''' 
        Turns the Robot relative to the angleRad, changing the set speed to speed
        
        @param angleRad describes desired turn, pos is CCW
        @param speed    describes set speed of motors in m/s
        @return state of execution
        ''' 
        return False
    
    def ChangeSpeed(self, speed):
        '''
        Changes overall speed set of bot
        
        @param speed describes set speed of motors in m/s
        @return state of execution
        '''
        
    def FireLeftMotor(self,time):
        '''
        Testing method that fires right motor for ___ time
        @return state of execution
        '''
        
    def FireRightMotor(self,time):
        '''
        Testing method that fires right motor for ___ time
        @return state of execution
        '''

    def GoStraight(self, doubleHere, doubleThere):
        self.FireLeftMotor(doubleHere)
        self.FireRightMotor(doubleThere)

        
