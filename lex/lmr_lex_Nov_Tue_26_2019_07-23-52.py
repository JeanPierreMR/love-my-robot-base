import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
	robot.turn_in_place(degrees(180), speed = degrees(100)).wait_for_completed()
cozmo.run_program(cozmo_program)
