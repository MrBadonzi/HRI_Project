import os, qi
from sonar import *
import argparse
import os
from naoqi import ALProxy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--project-path", type=str,
                        default="/home/robot/playground/HRI_Project/topics/welcome_topic.top")
   
    args = parser.parse_args()
    project_path = args.project_path


    pip = os.getenv('PEPPER_IP')
    pport = 9559
    url = "tcp://" + pip + ":" + str(pport)

    app = qi.Application(["App", "--qi-url=" + url ])
    app.start() # non blocking
    session = app.session
    memory_service = app.session.service("ALMemory")

    # sonar
    #EVENTUALMENTE PER CONNESSIONE IN REALE
    #sonar_service = session.service("ALSonar") 

    sonar = Sonar(memory_service)
    people_detected = sonar.peopleDetection()
    
    if people_detected:
        print("persona trovata")
        tts_service = session.service("ALTextToSpeech")
        tts_service.setLanguage("Italian")
        tts_service.setParameter("speed", 100)
        tts_service.say("Welcome! Can I help you?") #Benvenuto! Posso aiutarla?
        
        # FORSE SERVE IN REALE
        # asr = ALProxy("ALSpeechRecognition", pip , 9559)
        # vocabulary = ["hello", "what", "I don't understand", "english", "can you speak in eanglish", "can you talk in eanglish"]
        # asr.setVocabulary(vocabulary, False)
        # asr.subscribe("Test_ASR")
        
        
        # response = memory_service.getData("WordRecognized")
        # if response:
        #     print("User responded:", response)
        

        #asr.unsubscribe("Test_ASR")

   
        ALDialog = session.service("ALDialog")
        ALDialog.setLanguage("English")

       
        # Loading the topic given by the user (absolute path is required)
        topf_path = project_path.decode('utf-8')
        topic_name = ALDialog.loadTopic(topf_path.encode('utf-8'))

        # Activating the loaded topic
        ALDialog.activateTopic(topic_name)

        # Starting the dialog engine - we need to type an arbitrary string as the identifier
        # We subscribe only ONCE, regardless of the number of topics we have activated
        ALDialog.subscribe('my_dialog_example')

        try:
            raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")
        
        finally:
            # stopping the dialog engine
            ALDialog.unsubscribe('my_dialog_example')

            # Deactivating the topic
            ALDialog.deactivateTopic(topic_name)

            # now that the dialog engine is stopped and there are no more activated topics,
            # we can unload our topic and free the associated memory
            ALDialog.unloadTopic(topic_name)

   
    app.run() # blocking
