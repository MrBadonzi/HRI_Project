from motion import *
from database import *
from sonar import *

class Dialog():
    def __init__(self, memory_service, session, tts_service, ALDialog, topic_name, sonar):
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

    def handleNumber(self, lastInput):
        if lastInput.isdigit():
            if self.freeTables:
                tablet_motion(self.session, self.tts_service)
            else:
                sad_motion(self.session, self.tts_service ,table=True)

    def handleSentence(self, currentSentence):
        if "sorry" in currentSentence.lower() and "experience" in currentSentence.lower():
            sad_motion(self.session, self.tts_service)
            #TODO: INSERIRE OCCHI ROSSI
            
        elif "improve" in currentSentence.lower():
            neutral_motion(self.session)
            #TODO: INSERIRE OCCHI bianchi
            
        
        elif "yay" in currentSentence.lower():
            happy_motion(self.session)
            #TODO: INSERIRE OCCHI verdi
            
        
        elif "name" in currentSentence.lower() and "reservation" in currentSentence.lower():
            self.idLastInput =  self.lastInput.signal.connect(self.handleName)
        
        elif "day" in currentSentence.lower() and "nice" in currentSentence.lower():
            neutral_motion(self.session)
            #TODO: INSERIRE OCCHI bianchi
            
    def handleName(self, lastInput):
        res_found = False
        for elem in self.data:
            if lastInput == elem.getName().lower():
                table = elem.getTable()
                tablet_motion(self.session, self.tts_service)
                res_found = True
                break
        if not res_found:
            sad_motion(self.session, self.tts_service ,reservation=True)

        self.lastInput.signal.disconnect(self.idLastInput)