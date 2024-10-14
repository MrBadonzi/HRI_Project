import os, sys
from textblob import TextBlob
from polyglot.detect import Detector
from sonar_human_detection import sonar_detection

pdir = os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pdir+ '/cmd_server')
import pepper_cmd
from pepper_cmd import *

if __name__ == "__main__":
    begin() # connect to robot/simulator with IP in PEPPER_IP env variable

    # see pepper_tools/cmd_server/pepper_cmd.py
    pepper_cmd.robot.startSensorMonitor()

    # wait until front sonar detect something (range < 1.0)
    # personHere = False
    # while not personHere:
    #     p = pepper_cmd.robot.sensorvalue()
    #     personHere = p[1]<1.0 and  p[1]!=0  # front sonar
    personHere = False
    while not personHere:
        personHere = sonar_detection()
    # speech synthesis
    pepper_cmd.robot.say("Benvenuto! Posso aiutarla?")

    # speech recognition
    # vocabulary = list of keywords, e.g. ["yes", "no", "please"]
    vocabulary = ["si", "no"]
    timeout = 30 # seconds after function returns
    answer = pepper_cmd.robot.asr(vocabulary,timeout)
    if answer!="":  # valid answer
        lang_dict = Detector(answer).language
        if lang_dict.code == 'en':
            pepper_cmd.robot.say("Welcome! Can I help you?")
        elif lang_dict.code == 'it':
            if answer == 'si': #TODO: gestire tutte le risposte positive
              pepper_cmd.robot.say("Vuole accomodarsi o vuole vedere il menu?")
            elif answer == 'no':  #TODO: gestire tutte le risposte negative
                pepper_cmd.robot.say("Okay, scusi il disturbo")  
        else:
            pepper_cmd.robot.say("Sorry, I only speak Italian and English")

    pepper_cmd.robot.stopSensorMonitor()


    end()