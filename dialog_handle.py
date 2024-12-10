from motion import *
from database import *
from sonar import *
import time

class Dialog():
    def __init__(self, memory_service, session, tts_service, ALDialog, topic_name, sonar, tablet):
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
        self.sonar = sonar
        self.tablet = tablet

    def handleNumber(self, lastInput):
        #print(lastInput)
        numbers = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}
        if lastInput.lower() in numbers:
            if self.freeTables:
                self.tts_service.say("The table displayed on the screen is ready for you, please take your seat.")
                tablet_motion(self.session, self.tts_service, self.tablet)
            else:
                sad_motion(self.session, self.tts_service ,self.tablet, table=True)

    def handleSentence(self, currentSentence):
        #print(currentSentence)

        if "sorry" in currentSentence.lower():# and "experience" in currentSentence.lower():
            sad_motion(self.session, self.tts_service, self.tablet)
            
        elif "improve" in currentSentence.lower():
            neutral_motion(self.session)            
        
        elif "yay" in currentSentence.lower():
            happy_motion(self.session)
            
        
        elif "name" in currentSentence.lower() and "reservation" in currentSentence.lower():
            self.idLastInput =  self.lastInput.signal.connect(self.handleName)

        elif "displayed" in currentSentence.lower():
            tablet_motion(self.session, self.tts_service, self.tablet)
        
        elif "day" in currentSentence.lower() and "nice" in currentSentence.lower():
            neutral_motion(self.session)

            
    def handleName(self, lastInput):
        res_found = False
        #print(lastInput)
        for elem in self.data:
            #print(elem.getName().lower())
            if lastInput.lower() == elem.getName().lower():
                table = elem.getTable()
                self.tts_service.say("The table displayed on the screen is ready for you, please take your seat.")
                tablet_motion(self.session, self.tts_service, self.tablet)
                res_found = True
                break
        if not res_found:
            sad_motion(self.session, self.tts_service ,self.tablet, reservation=True)

        self.lastInput.signal.disconnect(self.idLastInput)