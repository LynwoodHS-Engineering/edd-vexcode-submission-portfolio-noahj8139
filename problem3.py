#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
servo_a = Servo(brain.three_wire_port.a)
servo_b = Servo(brain.three_wire_port.b)


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
#   Project:      Rings of Power
#   Author:       Noah Jimenez-Calleja & Kevyn Aguilar
#   Created:
#   Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
servo_b.set_position(-30,DEGREES)
wait(2,SECONDS)
servo_a.set_position(27,DEGREES)
wait(0.6,SECONDS)
servo_a.set_position(22,DEGREES)
wait(1,SECONDS)
servo_b.set_position(30,DEGREES)
wait(1,SECONDS)
servo_a.set_position(50,DEGREES)
wait(3,SECONDS)
servo_b.set_position(-30,DEGREES)
