import cozmo
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_program(robot: cozmo.robot.Robot):
	robot.pop_a_wheelie(robot.world.get_light_cube(3)).wait_for_completed()
	robot.say_text('Oh oh, nop').wait_for_completed()
	robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabSurprise).wait_for_completed()
	robot.drive_wheels(-100, 100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3)
	robot.drive_wheels(100, -100, l_wheel_acc=999, r_wheel_acc=999, duration=0.6)
	robot.drive_wheels(-100, 100, l_wheel_acc=999, r_wheel_acc=999, duration=0.3)
	robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWhee1).wait_for_completed()
	robot.set_lift_height(1.0, accel=100.0, max_speed=100.0).wait_for_completed()
	robot.set_lift_height(0.0, accel=100.0, max_speed=100.0).wait_for_completed()
	robot.drive_wheels(-200, -200, l_wheel_acc=9999, r_wheel_acc=9999, duration=0.5)
	time.sleep(1)
	robot.say_text('Ooo YES').wait_for_completed()
cozmo.run_program(cozmo_program)
