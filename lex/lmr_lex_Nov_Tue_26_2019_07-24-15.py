import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
	robot.pickup_object(robot.world.get_light_cube(3), num_retries=2).wait_for_completed()
cozmo.run_program(cozmo_program)
