import time
import os
import datetime


class transpilator:
    
    #region Start
    def __init__(self):
        self.update_file()
        self.instructions = {
            #actions
            "PRINT": self.write_print, "MATH": self.write_math_say, "YES": self.write_say(["yes"]), "SOUND": self.write_song
            #drive

            #animations
            }
    def update_file(self):
        now = datetime.datetime.now()
        file_name = "lmr_lex_"+ now.strftime("%b_%a_%d_%Y_%H-%M-%S")+".py"
        self.py_file = open(file_name, 'w+')
    #endregion
    #region dev tools
    def write_set(self, arg_list):
        varname= arg_list[0]
        self.py_file.write(varname+"="+arg_list[1]+"\n")
    def write_print(self, arg_list):
        printing_str= arg_list[0]
        printing_str = arg_list.pop(0)
        for arg in arg_list:
            printing_str = printing_str +" "+arg
        self.py_file.write("print('"+printing_str+"')\n")
    #endregion
    #region writter()

    def write_say(self, arg_list, wait = True):
        '''say_text and wait for it to end'''
        lines = arg_list.pop(0)
        for arg in arg_list:
            lines = lines +" "+arg
        if(wait):
            self.py_file.write("robot.say_text('"+lines+"').wait_for_completed()\n")
        elif(wait):
            self.py_file.write("robot.say_text('"+lines+"')\n")
    def write_math_say(self, arg_list):
        '''does math by eval'''
        operation = arg_list.pop(0)
        for arg in arg_list:
            operation = operation +" "+arg
        print("test")
        print(operation)
        self.write_say([str(eval(operation))]) 
    def write_count(self, arg_list):
        '''does math by eval'''
        last_number = int(arg_list.pop(0))+1
        self.py_file.write("for i in range(1,"+str(last_number)+"):\n")
        self.py_file.write("    robot.say_text(str(i)).wait_for_completed()\n")
    def write_sound(self, arg_list):
        code_str = "# This sound MusicStyle80S2159BpmLoop is:"\
                "#   - 80S style music #2, at 159Bpm (beats per minute)"\
                "#   - if the song is played repeatedly, the beginning and end"\
                "#     line up making it possible to play in a Loop"\
                "robot.play_audio(cozmo.audio.AudioEvents.MusicStyle80S2159BpmLoop)"
        self.py_file.write(code_str + "\n")
    def write_song(self, arg_list):
        code_str = """notes = [
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
    
    def write_drive(self, arg_list):
        self.py_file.write("robot.drive_straight(distance_mm("+arg_list[0]+"), speed_mmps("+arg_list[1]+")).wait_for_completed()\n")
    def write_turn(self,arg_list):
        self.py_file.write("robot.turn_in_place(degrees("+arg_list[0]+"), speed = degrees(" + arg_list[1] + ")).wait_for_completed()\n")
    
    def write_off_charger(self):
        self.py_file.write("robot.drive_off_charger_contacts().wait_for_completed()\n")
    def lift(self, amount):
        self.py_file.write("robot.say_text('"+str(amount/100)+"').wait_for_completed()\n")
    

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
                print("try: ")
                print(line)
                
                instruction = line.pop(0).upper()
                print(instruction)
                print(line)
                print("end try")
                self.instructions[instruction](line)
            except Exception as e:
                print(e)
                print("error inside " + str(line))

    
        
    

simple_code = " print x as 1 2\n math 1 + 4\nsound\nyes"



transpilator1 = transpilator()
transpilator1.transpile(simple_code)
# check_code(instructionlist)
# write_file(instructionlist)