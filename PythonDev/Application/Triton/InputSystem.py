'''
Created on Feb 4, 2020

@author: matt
'''

class InputSystem(object):
    '''
    classdocs
    '''


    def __init__(self, GPSPort, accelPort, plasticLevelPort, batLevelPort):
        '''
        Constructor
        '''
        self.gpsPort = GPSPort
        self.accel = plasticLevelPort
        self.plasticLevel = plasticLevelPort
        self.batterylvl = batLevelPort
        
    def setupProperties(self):
        '''
        batteryislow & plasticFullProperties to be added
        @postcondition: Properties will not be null
        '''
        
        
    def getGPS(self):
        gpsOutput = gpsPort
        print("The gps port is on: " + gpsOutput)
        
    def UpdateValues(self):
        '''
        Updates all read values, and sends to log file
        
        @postcondition: All input parameters will be updated with current values, or made null
        if unable to refresh.  Old Values will be sent to file
        @return: boolean status of excecution
        '''
        gpsOutput = self.getGPS()
        accelOutput = self.getAccel()
        battVolt = self.getbattVoltage()
        plasticLvl = self.getPlasticLevel()
        
