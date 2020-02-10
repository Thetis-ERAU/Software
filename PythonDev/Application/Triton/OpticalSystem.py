'''
Created on Feb 4, 2020

@author: matt
'''

class OpticalSystem(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.cameraPort = None
        self.lidarPort = None
        self.objectPositions = None
    
    def detectObjects(self):
        self.objectPositions = None
        
    def trackObjects(self):
        self.objectPositions = None
        
    def getObjects(self):
        '''
        @return 2xn array of positions
        '''
    def isWorking(self):
        '''
        @return camera's current operations
        '''