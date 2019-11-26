import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
	robot.drive_straight(distance_mm(5), speed_mmps(10)).wait_for_completed()
cozmo.run_program(cozmo_program)
