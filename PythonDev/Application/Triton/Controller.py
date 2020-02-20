'''
Created on Feb 4, 2020

@author: matt
'''
from multiprocessing import Process
import sched
import time
from InputSystem import *
from DriveSystem import *
from OpticalSystem import *
from SandSystem import *
from HelperClasses import RepeatedTimer


inputRefreshPeriod = 2000 # 500 ms

def DriveLoop():
    '''
    '''
    print("in driveloop")
    driveSystem = DriveSystem(0)
        
def OpticalLoop():
    '''
    '''
    print("in opticalloop")
    opticalSystem = OpticalSystem(0)
        
def SandLoop():
    '''
    '''
    print("in sandloop")
    sandSystem = SandSystem(0)
        
def InputLoop():
    '''
    '''
    print("in inputloop")
    inputSystem = InputSystem(inputRefreshPeriod)
    refreshInputs = RepeatedTimer(inputRefreshPeriod, inputSystem.updateValues)

  
        
        
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

