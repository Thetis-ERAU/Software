'''
Created on Feb 4, 2020

@author: matt
'''
from multiprocessing import Process
def DriveLoop():
        '''
        '''
        print("in driveloop")
        
def OpticalLoop():
        '''
        '''
        print("in opticalloop")
        
def SandLoop():
        '''
        '''
        print("in sandloop")
        
def InputLoop():
        '''
        '''
        print("in inputloop")
        
#Start MultiProcessing Loops
if __name__ == '__main__':
    # freeze_support()
    DriveProcess = Process(target = DriveLoop)
    OpticalProcess = Process(target = OpticalLoop)
    SandProcess = Process(target = SandLoop)
    InputProcess = Process(target = InputLoop)

    DriveProcess.start()
    OpticalProcess.start()
    SandProcess.start()
    InputProcess.start()

