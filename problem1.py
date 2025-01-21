#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
bumper_a = Bumper(brain.three_wire_port.a)
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
distance_2 = Distance(Ports.PORT2)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      Sensor to Actuator Project
#	Author:       Noah Jimenez-Calleja & Kevyn Aguilar
#	Created:      1/17/25
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
Xdist = distance_2.object_distance(INCHES)

while True:
    pass

    Xdist = distance_2.object_distance(INCHES)
    brain.screen.print("Current Distance:")
    brain.screen.next_row()
    brain.screen.print(Xdist)

    if distance_2.object_distance(INCHES) >= 10:

            motor_1.set_velocity(0, PERCENT)
            motor_1.stop()

    else:

        pass

        motor_1.set_velocity(50, PERCENT)
        motor_1.spin(FORWARD)

    pass
