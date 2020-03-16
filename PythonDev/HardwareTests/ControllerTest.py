import inputs
import sys
import time

try:
    events = inputs.get_gamepad()
    try:
        while True:
            events = inputs.get_gamepad()
            #time.sleep(.1)
            for event in events:
                for key, value in event.state.items():
                    output_string += key + ':' + str(value) + ' '
                print(output_string)

    except KeyboardInterrupt:
        pass

except inputs.UnpluggedError:
    print("I can't find a gamepad, exiting now")

