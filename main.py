# Library imports
from vex import *
import random

# Setup Brain and Brain Inertial
brain=Brain()
Brain_Inertial = Inertial

# Robot configuration code
left_drive_smart = Motor(Ports.PORT1, 1, False)
right_drive_smart = Motor(Ports.PORT6, 1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 200, 200, 200, DistanceUnits.MM)

touchled_2 = Touchled(Ports.PORT2)
optical_3 = Optical(Ports.PORT3)
distance_7 = Distance(Ports.PORT7)
bumper_8 = Bumper(Ports.PORT8)
controller = Controller()


# Setup
drivetrain.set_drive_velocity(100, PERCENT)
drivetrain.set_turn_velocity(100, PERCENT)

direction = [LEFT, RIGHT, FORWARD, REVERSE]

# Main function

while touchled_2.pressing() == False:
    wait(10, MSEC)
    brain.screen.print("Press the touchled to start")
brain.screen.clear_screen()
brain.screen.print("Starting")

current_distance = distance_7.object_distance(MM)
distance_to_go = random.randint(50, 100)

drivetrain.drive_for(FORWARD, current_distance+distance_to_go, DistanceUnits.MM)
while bumper_8.pressing() == False:
    drivetrain.drive(REVERSE)
drivetrain.stop()

while True:

    # Choose what direction to go
    to_go = random.choice(direction)

    distance_to_go = random.randint(50, 100)
    degrees_to_turn = random.randint(30, 90)
    if to_go == LEFT or to_go == RIGHT:
        # Turn for a random angle
        drivetrain.turn_for(to_go, degrees_to_turn, RotationUnits.DEG)
    degrees_to_turn = random.randint(30, 90)
    brain.screen.print(degrees_to_turn)
    if to_go == LEFT or to_go == RIGHT:
        # Turn for a random angle
        drivetrain.turn_for(to_go, degrees_to_turn, RotationUnits.DEG)
    elif to_go == FORWARD or to_go == REVERSE:
        # Drive for a random distance
        drivetrain.drive_for(to_go, distance_to_go, DistanceUnits.MM)
        # Drive for a random distance
        drivetrain.drive_for(to_go, distance_to_go, DistanceUnits.MM)
    else:
        brain.screen.print("Error")
        break
    # Check if red donut is detected
    if optical_3.color() == "red":
        brain.screen.print("Red Donut Detected")
        drivetrain.turn_for(RIGHT, 900, RotationUnits.DEG)
        break
    brain.screen.clear_screen()