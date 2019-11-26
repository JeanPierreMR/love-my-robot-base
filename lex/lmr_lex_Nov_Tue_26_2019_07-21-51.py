import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
	robot.say_text('Something').wait_for_completed()
	for i in range(1,4):
	    robot.say_text(str(i)).wait_for_completed()
cozmo.run_program(cozmo_program)
	robot.say_text('Something').wait_for_completed()
	for i in range(1,4):
	    robot.say_text(str(i)).wait_for_completed()
cozmo.run_program(cozmo_program)
