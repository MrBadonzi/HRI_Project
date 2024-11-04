from motion import *
from database import *

class Dialog():
    def __init__(self, memory_service, session, tts_service, ALDialog, topic_name):
        # Get the services ALMemory, ALTextToSpeech.
        # touch sensors
        self.lastInput = memory_service.subscriber("Dialog/LastInput")

        self.idLastInputNumber = self.lastInput.signal.connect(self.handleNumber)

        self.currentSentence = memory_service.subscriber('ALTextToSpeech/CurrentSentence')

        self.currentSentence.signal.connect(self.handleSentence)

        
        database = Database()
        self.data = database.getDatabase()
        tab = Table()
        self.table = tab.getTables()

        self.freeTables = getFreeTables(self.table, self.data)

        self.session = session
        self.tts_service = tts_service
        self.ALDialog = ALDialog
        self.topic_name = topic_name

    def handleNumber(self, lastInput):
        if lastInput.isdigit():
            if self.freeTables:
                #tts_service.say("The table displayed on the screen is ready for you, please take your seat." + str(freeTables.pop()))
                tablet_motion(self.session, self.tts_service)
            else:
                #tts_service.say("I'm sorry, there are no available tables")
                sad_motion(self.session, self.tts_service ,table=True)

    def handleSentence(self, currentSentence):
        print(currentSentence)
        if "sorry" in currentSentence.lower() and "experience" in currentSentence.lower():
            sad_motion(self.session, self.tts_service)
            #TODO: INSERIRE OCCHI ROSSI
            stop_flag = True
            # Stop the dialog engine
            self.ALDialog.unsubscribe('my_dialog_example')
            # Deactivate and unload the main topic
            self.ALDialog.deactivateTopic(self.topic_name)
            self.ALDialog.unloadTopic(self.topic_name)
        
        elif "improve" in currentSentence.lower():
            neutral_motion(self.session)
            #TODO: INSERIRE OCCHI bianchi
            stop_flag = True
            # Stop the dialog engine
            self.ALDialog.unsubscribe('my_dialog_example')
            # Deactivate and unload the main topic
            self.ALDialog.deactivateTopic(self.topic_name)
            self.ALDialog.unloadTopic(self.topic_name)
        
        elif "yay" in currentSentence.lower():
            happy_motion(self.session)
            #TODO: INSERIRE OCCHI verdi
            stop_flag = True
            # Stop the dialog engine
            self.ALDialog.unsubscribe('my_dialog_example')
            # Deactivate and unload the main topic
            self.ALDialog.deactivateTopic(self.topic_name)
            self.ALDialog.unloadTopic(self.topic_name)
        
        elif "name" in currentSentence.lower() and "reservation" in currentSentence.lower():
            self.idLastInput =  self.lastInput.signal.connect(self.handleName)
        
        elif "day" in currentSentence.lower():
            neutral_motion(self.session)
            #TODO: INSERIRE OCCHI bianchi
            stop_flag = True
            # Stop the dialog engine
            self.ALDialog.unsubscribe('my_dialog_example')
            # Deactivate and unload the main topic
            self.ALDialog.deactivateTopic(self.topic_name)
            self.ALDialog.unloadTopic(self.topic_name)


    def handleName(self, lastInput):
        res_found = False
        for elem in self.data:
            if lastInput == elem.getName().lower():
                table = elem.getTable()
                tablet_motion(self.session, self.tts_service)
                #tts_service.say("The table displayed on the screen is ready for you, please take your seat." + str(table))
                res_found = True
                break
        if not res_found:
            #tts_service.say("I don't have any reservation with that name. I will contact someone")
            sad_motion(self.session, self.tts_service ,reservation=True)

        stop_flag = True
        # Stop the dialog engine
        self.ALDialog.unsubscribe('my_dialog_example')
        # Deactivate and unload the main topic
        self.ALDialog.deactivateTopic(self.topic_name)
        self.ALDialog.unloadTopic(self.topic_name)

        self.lastInput.signal.disconnect(self.idLastInput)