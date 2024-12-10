# TODO: 
# 
#  
import os, qi
from sonar import *
from database import *
import argparse
import os
from naoqi import ALProxy
from motion import *
from touch import *
from dialog_handle import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #IN REALE PATH == /home/nao/temp/HRI/welcome_topic.top
    #IN SIMULATA == /home/robot/playground/HRI_Project/topics/welcome_topic.top
    parser.add_argument("--project-path", type=str,
                        default="/home/robot/playground/HRI_Project/topics/welcome_topic.top")  # pepper/.../ prova_topic.top #/playground/HRI_Project/topics
    parser.add_argument("--tablet", action='store_true', help="Set tablet flag to True")

    args = parser.parse_args()
    project_path = args.project_path
    tablet = args.tablet
    
    pip = os.getenv('PEPPER_IP') #"10.0.1.201"  #"10.0.1.201" #
    pport = 9559
    url = "tcp://" + pip + ":" + str(pport)

    app = qi.Application(["App", "--qi-url=" + url])
    app.start()  # non blocking
    session = app.session
    memory_service = app.session.service("ALMemory")

    # sonar
    # EVENTUALMENTE PER CONNESSIONE IN REALE
    # sonar_service = session.service("ALSonar")

    sonar = Sonar(memory_service)
    people_detected = sonar.peopleDetection()

    if people_detected:
        print("persona trovata")
        tts_service = session.service("ALTextToSpeech")
        tts_service.setLanguage("English")  # Italian
        tts_service.setParameter("speed", 100)
        tts_service.say("Welcome! Can I help you?")  # Benvenuto! Posso aiutarla?

        # FORSE SERVE IN REALE
        # asr_service = session.service("ALSpeechRecognition")

        # asr_service.setLanguage("English")

        # # Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
        # vocabulary = ["yes", "no", "menu", "seat", "bad", "fine", "excellent", "sure", "I would like to take a seat", "I would like to look at the menu", "I would like to leave a review", "bad", "fine", "excellent", "it was bad", "it was fine", "it was excellent", "totti", "four","jacob"]
        # asr_service.setVocabulary(vocabulary, False)

        # # Start the speech recognition engine with user Test_ASR
        # asr_service.subscribe("Test_ASR")
        # response = memory_service.getData("WordRecognized")
        # print("User responded:", response)
        # print('Speech recognition engine started')
        # #time.sleep(20)
        # asr_service.unsubscribe("Test_ASR")



        ALDialog = session.service("ALDialog")
        ALDialog.setLanguage("English")

        # Loading the topic given by the user (absolute path is required)
        topf_path = project_path.decode('utf-8')
        topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))

        touch = Touch(memory_service, session, tts_service, ALDialog, topf_path)

        # Activating the loaded topic
        ALDialog.activateTopic(topic_name)

        # Starting the dialog engine - we need to type an arbitrary string as the identifier
        # We subscribe only ONCE, regardless of the number of topics we have activated
        ALDialog.subscribe('my_dialog_example')

        dialog = Dialog(memory_service, session, tts_service, ALDialog, topic_name, sonar, tablet)


        ########  START TABLET  ##########
        if tablet:
            os.system("python modim/demo/scripts/demo1.py")

        else:


            try:
                
                value = raw_input("\nSpeak to the robot using rules from the just loaded .top file:")
            
            except KeyboardInterrupt:

                stop_flag = True
                # Stop the dialog engine
                ALDialog.unsubscribe('my_dialog_example')
                # Deactivate and unload the main topic
                ALDialog.deactivateTopic(topic_name)
                ALDialog.unloadTopic(topic_name)  

        
    app.run()  # blocking
