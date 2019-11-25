import time
import os
import datetime
import subprocess

class transpilator:
    
    #region Start
    def __init__(self):
        self.update_file()
        self.instructions = {
            #actions
            "PRINT": self.write_print, "WAIT": self.write_wait, "SAY": self.write_say, 
            "MATH": self.write_math_say,"COUNT":self.write_count, "YES": write_yes, "SOUND": self.write_sound,
            #drive
            "DRIVE_OFF": self.write_off_charger, "MOVE": self.write_drive, 
            "TURN": self.write_turn, "LIFT": self.write_lift,
            #animations
            "LIGHT": self.write_lights, "CUBE_LIGHT": self.write_lights_cube, "PICKUP": self.write_pick_cube,
            "DROP":self.write_drop_cube, "ROLL_CUBE":self.write_roll_cube, "WHEELIE": self.write_wheelie

            }
    def update_file(self):
        now = datetime.datetime.now()
        self.file_name = "lmr_lex_"+ now.strftime("%b_%a_%d_%Y_%H-%M-%S")+".py"
        self.py_file = open(self.file_name, 'w+')
        self.py_file.write("import cozmo\n")
        self.py_file.write("import time\n")
        self.py_file.write("def cozmo_program(robot: cozmo.robot.Robot):\n")

    #endregion
    #region dev tools
    def write_set(self, arg_list):
        varname= arg_list[0]
        self.py_file.write("\t"+varname+"="+arg_list[1]+"\n")
    def write_print(self, arg_list):
        printing_str= arg_list[0]
        printing_str = arg_list.pop(0)
        for arg in arg_list:
            printing_str = printing_str +" "+arg
        self.py_file.write("\t"+"print('"+printing_str+"')\n")
    def write_wait(self, secs):
        self.py_file.write("\t"+"time.sleep("+ str(secs)+ ")")
    #endregion
    #region writter()
    def write_yes(self, arg_list):
        self.write_say(["yes"], wait=False)
        self.py_file.write("\t"+"robot.move_head(-5)")
        self.py_file.write("\t"+"robot.move_head(5)")
        self.py_file.write("\t"+"robot.move_head(-5)")
        self.py_file.write("\t"+"robot.move_head(0)")

    def write_say(self, arg_list, wait = True):
        '''say_text and wait for it to end'''
        lines = arg_list.pop(0)
        for arg in arg_list:
            lines = lines +" "+arg
        if(wait):
            self.py_file.write("\t"+"robot.say_text('"+lines+"').wait_for_completed()\n")
        elif(wait):
            self.py_file.write("\t"+"robot.say_text('"+lines+"')\n")
    def write_math_say(self, arg_list):
        '''does math by eval'''
        operation = arg_list.pop(0)
        for arg in arg_list:
            operation = operation +" "+arg
        print("test")
        print(operation)
        self.write_say("\t"+[str(eval(operation))]) 
    def write_count(self, arg_list):
        '''does math by eval'''
        last_number = int(arg_list.pop(0))+1
        self.py_file.write("\t"+"for i in range(1,"+str(last_number)+"):\n")
        self.py_file.write("\t"+"    robot.say_text(str(i)).wait_for_completed()\n")
    def write_sound(self, arg_list):
        # "# This sound MusicStyle80S2159BpmLoop is:"+\
        #         "#   - 80S style music #2, at 159Bpm (beats per minute)"+\
        #         "#   - if the song is played repeatedly, the beginning and end"+\
        #         "#     line up making it possible to play in a Loop"+\
        code_str = "\t"+"robot.play_audio(cozmo.audio.AudioEvents.MusicTinyOrchestraInit)\n"
        code_str = code_str + "\t"+ "robot.play_audio(cozmo.audio.AudioEvents.MusicTinyOrchestraBassMode1)\n"
        code_str = code_str + "\t"+ "time.sleep(2.0)\n"
        code_str = code_str + "\t"+ "robot.play_audio(cozmo.audio.AudioEvents.MusicTinyOrchestraStop)\n"

        self.py_file.write(code_str)
    def write_song(self, arg_list):
        code_str = "\t"+"""notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.Rest, cozmo.song.NoteDurations.Quarter) ]
        robot.play_song(notes, loop_count=1).wait_for_completed()"""
        self.py_file.write(code_str + "\n")
    #region drive
    def write_drive(self, arg_list):
        self.py_file.write("\t"+"robot.drive_straight(distance_mm("+arg_list[0]+"), speed_mmps("+arg_list[1]+")).wait_for_completed()\n")
    def write_turn(self,arg_list):
        self.py_file.write("\t"+"robot.turn_in_place(degrees("+arg_list[0]+"), speed = degrees(" + arg_list[1] + ")).wait_for_completed()\n")
    
    def write_off_charger(self, arg_list = []):
        self.py_file.write("\t"+"robot.drive_off_charger_contacts().wait_for_completed()\n")
    def write_lift(self, arg_list):
        self.py_file.write("\t"+"robot.say_text('"+str(int(arg_list[0])/100)+"').wait_for_completed()\n")
    #endregion
    
    #region animations
    def write_lights(self, arg_list):
        self.py_file.write("\t"+"robot.set_all_backpack_lights(cozmo.lights."+arg_list[0].lower()+"_light)\n")
    def write_animation(self, arg_list):
        self.py_file.write("\t"+"robot.play_anim_trigger(cozmo.anim.Triggers."+arg_list[0]+").wait_for_completed())\n")
    def write_lights_cube(self, arg_list):
        self.py_file.write("\t"+"robot.world.get_light_cube("+arg_list[0]+").set_lights(cozmo.lights."+arg_list[1].lower()+"_light\n")
    def write_pick_cube(self, arg_list):
        self.py_file.write("\t"+"robot.pickup_object(robot.world.get_light_cube("+arg_list[0]+"), num_retries=2).wait_for_completed()\n")
    def write_drop_cube(self, arg_list):
        self.lift([0])
    def write_roll_cube(self, arg_list):
        self.py_file.write("\t"+"robot.roll_cube(robot.world.get_light_cube("+arg_list[0]+").wait_for_completed()\n")
    def write_wheelie(self, arg_list):
        self.py_file.write("\t"+"robot.pop_a_wheelie(robot.world.get_light_cube("+arg_list[0]+").wait_for_completed()\n")
    #endregion

    #endregion



    def check_code(self, instructionlist):
        i=0
        errores = []
        #checking error command not found
        while(i < len(instructionlist)):
            if(not(instructionlist[i][0] in self.instructions)):
                errores.append(i)
            i+=1
        if(errores):
            return errores
        else:
            return True
    def prepare_code(self, code):
        '''divides the code in a list of lists by its new lines and spaces'''
        linelist = code.strip().split("\n")
        instructionlist = []
        for line in linelist:
            line = line.strip().split(" ")
            instructionlist.append(line)
        return instructionlist
    def transpile(self, code):

        instructionlist = self.check_code(code)
        instructionlist = self.prepare_code(code)

        for line in instructionlist:
            try:
                instruction = line.pop(0).upper()
                self.instructions[instruction](line)
            except Exception as e:
                print(e)
                print("error inside " + str(line))
    def run(self):
        self.py_file.write("cozmo.run_program(cozmo_program)\n")
        code = self.py_file.read()
        print("\n\n\n")
        subprocess.run(["py", self.file_name])
    

    
if __name__ == "__main__":

    simple_code = " print x as 1 2\n math 1 + 4\nyes\n sound"



    transpilator1 = transpilator()
    transpilator1.transpile(simple_code)
    transpilator1.run()
