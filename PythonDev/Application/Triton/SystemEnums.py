from enum import Enum

class ValueEnum(Enum):
    GPS1 = 1
    GPS2 = 2
    ACC1 = 3
    ACC2 = 4
    ACC3 = 5
    VOLT = 6
    PLASTIC = 7
    INPUT_DRIVE = 8
    INPUT_TURN = 9

class BoolEnum(Enum):
    CAM_SIGNAL = 1
    VOLT_SIGNAL = 2
    ACC_SIGNAL = 3
    GPS_SIGNAL = 4
    LIDAR_SIGNAL = 5
    PLASTIC_SIGNAL = 6
    DRIVE1_SIGNAL = 7
    DRIVE2_SIGNAL = 8
