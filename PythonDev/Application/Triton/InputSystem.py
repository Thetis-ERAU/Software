'''
Created on Feb 4, 2020

@author: matt
'''

class InputSystem(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self._gpsAddress = None
        self._accel = None
        self._plasticLevel = None
        self._batteryLevel = None
        
    def setupProperties(self):
        '''
        batteryislow & plasticFullProperties to be added
        @postcondition: Properties will not be null
        '''
        
        
    def UpdateValues(self):
        '''
        Updates all read values, and sends to log file
        
        @postcondition: All input parameters will be updated with current values, or made null
        if unable to refresh.  Old Values will be sent to file
        @return: boolean status of excecution
        '''
    def getGPS(self):
        '''
        @return 1x2 array of gps coordinates
        '''
        return self._gpsAddress
    
    def getAccel(self):
        '''
        @return 1xn array of accel qualities
        '''
        return self._accel
    
    def getBattVolt(self):
        '''
        @return double of battery voltage
        '''
    def getPlasticLevel(self):
        '''
        @return double of plastic lvl
        '''