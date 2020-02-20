'''
Created on Feb 4, 2020

@author: matt
'''
import serial
import adafruit_gps
import time
import sched

class InputSystem(object):
    '''
    classdocs
    '''

    def __init__(self, gpsFreq = 1000):
        '''
        Constructor
        '''
        self.gpsFreq = gpsFreq  # in ms
        try:
            self.uart = serial.Serial('/dev/serial0', baudrate = 9600, timeout = 10)
            self.gps = adafruit_gps.GPS(uart, debut = False)
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
        self.gpsonline = self.setupGPS()


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
        allWorking = self.updateGPS()
        return allWorking

    def setupGPS(self):
        if self.gps is None:
            print("GPS has not been initialized, so SetupGPS in InputSystem cannot continue")
            return False;
        self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        self.gps.send_command(b'PMTK220,'+str(gpsFreq))
    
    def updateGPS(self):
        if self.gps is None:
            print("GPS has not been initialized, so updateGPS in InputSystem cannot continue")
            return False;
        self.gps.update()
        if self.gps.has_fix:
            for key in self.gpsDataDict.keys():
                self.DataDict[key] = gps.key
        else:
            for key in self.gpsDataDict.keys():
                self.DataDict[key] = -1


