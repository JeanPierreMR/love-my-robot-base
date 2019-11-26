import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
	robot.set_all_backpack_lights(cozmo.lights.green_light)
cozmo.run_program(cozmo_program)
