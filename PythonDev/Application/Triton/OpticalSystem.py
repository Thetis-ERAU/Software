'''
Created on Feb 4, 2020

@author: matt
'''

class OpticalSystem(object):
    '''
    classdocs
    '''


    def __init__(self, liPort, camPort, w, h):
        '''
        Constructor
        '''
        self.lidarPort = liPort
        self.cameraPort = camPort
        #How to create an array: https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
        objPosition = [w][h]
    def detectObject(self):
        #code here

    def trackObject(self):
        #Code here

    def getObjects(self,w,h):
        print("The object is at position " + objPosition[w][h])

    def recordData(self):
        #Code here

    def isWorking(self):
        #Code here
