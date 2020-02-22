'''
Created on Feb 4, 2020

@author: matt
'''
from multiprocessing import Process
import sched
import time
import keyboard
from InputSystem import *
from DriveSystem import *
from OpticalSystem import *
from SandSystem import *
from HelperClasses import RepeatedTimer


INPUT_REFRESH_PERIOD = 1000 #ms
MAIN_REFRESH_PERIOD = 250   #ms

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
    inputSystem = InputSystem(0)
    refreshInputs = RepeatedTimer(INPUT_REFRESH_PERIOD, inputSystem.updateValues) 



#Start MultiProcessing Loops
if __name__ == '__main__':

    inputSystem =InputSystem(0)
    refreshInputs = RepeatedTimer(1000, inputSystem.updateValues)

    # freeze_support()
    DriveProcess = Process(target = DriveLoop)
    OpticalProcess = Process(target = OpticalLoop)
    SandProcess = Process(target = SandLoop)
    InputProcess = Process(target = InputLoop)

    DriveProcess.dameon = True;
    OpticalProcess.dameon = True;
    SandProcess.daemon = True;
    InputProcess.daemon = True;

    DriveProcess.start()
    OpticalProcess.start()
    SandProcess.start()
    InputProcess.start()
    
    run = True
    #Main Loop
    while run == True and not keyboard.is_pressed('Escape'): #Not perfect, only ends when esc is held, not pressed
        time.sleep(MAIN_REFRESH_PERIOD/1000)



