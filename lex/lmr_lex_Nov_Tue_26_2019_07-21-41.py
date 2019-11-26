import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
	robot.say_text('Something').wait_for_completed()
cozmo.run_program(cozmo_program)
