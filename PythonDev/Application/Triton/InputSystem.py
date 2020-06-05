'''
Created on Feb 4, 2020

@author: matt
'''
import serial
import adafruit_gps
import signal, time
import inputs
import threading, _thread
from HelperClasses import EVENT_ABB
from contextlib import contextmanager


class TimeoutException(Exception): pass

class InputSystem(object):
    '''
    classdocs
    '''

    def __init__(self, gpsFreq = 1000,gpsPort = '/dev/serial0', accelPort = None, plasticLevelPort = None, batLevelPort = None):
        '''
        Constructor
        '''
        self.gpsUart = None
        self.gps = None

        self.gamepad = None
        self.gamepadState = {}
        self.oldGamepadEvents = {}
        self.gamepadAbbr = dict(EVENT_ABB)
        self._other = 0  #number of keyEvents that are not in EVENT_ABB

        self.accelPort = accelPort
        self.plasticLevelPort = plasticLevelPort
        self.batteryLevelPort = batLevelPort
        self.plasticLevel = None
        self.batteryLevel = None

        self.gpsOnline = self.setupGPS(gpsPort, gpsFreq)
        self.gamepadOnline = self.setupJoystick();


    def setupProperties(self):
        '''
        batteryislow & plasticFullProperties to be added
        @postcondition: Properties will not be null
        '''

    def updateValues(self):

        '''
        Updates all read values, and sends to log file
        @postcondition: All input parameters will be updated with current values, or made null
        if unable to refresh.  Old Values will be sent to file
        @return: boolean status of excecution
        '''
        print("The gps port is on: " + str(self.gpsUart))
        allWorking = self.updateGPS()
        #allWorking = self.updateJoystick()
        return allWorking

    @contextmanager
    def time_limit(self, seconds):
        timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
        timer.start()
        try:
            yield
        except KeyboardInterrupt:
            print("handling it")
            raise TimeoutException()
        finally:
            # if the action ends in specified time, timer is canceled
            timer.cancel()

    def setupGPS(self, gpsPort, gpsFreq):
        '''
        Connects to a GPS at gpsPort and requests pings at gpsFreq
        @return gps connection status
        '''
        try:
            self.gpsUart = serial.Serial(gpsPort, baudrate = 9600, timeout = 10)
            self.gps = adafruit_gps.GPS(self.gpsUart, debug = False)
        except serial.SerialException:
            self.gps = None
            print("GPS connection failed, Serial Exception raised")  
            
        self.gpsDataDict = {'_uart': -1,
                            'latitude': -1, 
                            'longitude': -1, 
                            'fix_quality': -1,
                            'fix_quality_3d': -1,
                            'altitude_m': -1,
                            'debug': -1,
                            'timestamp_utc': -1,
                            'satellites': -1,
                            'satellites_prev': -1,
                            'speed_knots': -1,
                            'height_geoid': -1,
                            'track_angle_deg': -1,
                            'sats': -1,
                            'sel_mode': -1,
                            'sat_prns': -1,
                            'true_track': -1,
                            'isactivedata': -1,
                            }

        if self.gps is None:
            print("GPS has not been initialized, so SetupGPS in InputSystem cannot continue")
            return False;
        self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        self.gps.send_command(b'PMTK220,'+bytes(gpsFreq))
        return True
    
    def updateGPS(self):
        '''
        Refreshes dataDict with updated data from the gps if connected
        '''
        if self.gps is None:
            print("GPS has not been initialized, so updateGPS in InputSystem cannot continue")
            return False;
        self.gps.update()
        if self.gps.has_fix:
            for key in self.gpsDataDict.keys():
                self.gpsDataDict[key] = self.gps.key
        else:
            for key in self.gpsDataDict.keys():
                self.gpsDataDict[key] = -1

    def setupJoystick(self):
        '''
        Connects a gamepad if connected
        @return gamepad connection status
        '''
        try:
            self.gamepad = inputs.devices.gamepads[0]
        except IndexError:
            self.gamepad = None
            self.gamepadOnline = False
            print("Gamepad not found, InputSystem cannot continue setupGamepad")
            return False
        return True

    def updateJoystick(self):
        '''
        Updates joystick values
        @return state of excecution
        '''
        if self.gamepad is None:
            return
        elif not self.gamepadOnline:
            self.setupJoystick()
            return False

        try:
            events = self.gamepad.read()
        except EOFError:
            events = []
        except inputs.UnpluggedError:
            print("Index Error due to gamepad not found, idling until found again")
            self.gamepadOnline = false
            return false

        for event in events:
            if event.ev_type =='Sync' or event.ev_type =='Misc':
                return
            key = event.ev_type + '-' + event.code
            
            try:
               abbv = self.gamepadAbbr[key]
            except KeyError:
                    abbv = self.handle_unknown_event(event, key)
                    if not abbv: return
            
            if event.ev_type =='Key' or event.ev_type == 'Absolute':
                if event.state is not None:
                    self.gamepadState[abbv] = event.state
        #print(self.strJoystickState())

    def handle_unknown_event(self, event, key):
        """Deal with unknown events."""
        if event.ev_type == 'Key' or event.ev_type == 'Absolute':
            new_abbv = 'B' + str(self._other)
            self.gamepadState[new_abbv] = 0
            self.oldGamepadEvents[new_abbv] = 0

        else:
            return None
        self.gamepadAbbr[key] = new_abbv
        self._other += 1

        return self.gamepadAbbr[key]

    def strJoystickState(self):
        """Format the state."""
        output_string = ""
        #for key, value in self.gamepadState.items():
        #    output_string += key + ':' + '{:>4}'.format(str(value) + ' ')

        for key, value in self.gamepadState.items():
            output_string += key + ':' + str(value) + ' '

        return output_string
   

    


