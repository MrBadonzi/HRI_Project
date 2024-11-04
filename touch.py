class Touch:
    def __init__(self, memory_service, session, tts_service, ALDialog, topf_path):
        # Get the services ALMemory, ALTextToSpeech.
        # touch sensors
        self.touch_service = session.service("ALTouch")

        # callback function
        self.anyTouch = memory_service.subscriber("TouchChanged")
        self.idAnyTouch = self.anyTouch.signal.connect(self.onTouched)
        
        self.tts_service = tts_service
        self.ALDialog = ALDialog
        self.topf_path = topf_path


    def onTouched(self, value):
        """ This will be called each time a touch
        is detected.

        """
        # Disconnect to the event when talking,
        # to avoid repetitions
        for p in value:
            if p[1]:
                self.tts_service.say("Nice to meet you, I am Pepper. Can I help you?")
                stop_flag = True
                # Stop the dialog engine
                self.ALDialog.unsubscribe('my_dialog_example')
                # Deactivate and unload the main topic
                topic_name = self.ALDialog.loadTopic(self.topf_path.encode('utf-8'))
                self.ALDialog.deactivateTopic(topic_name)
                self.ALDialog.unloadTopic(topic_name)  
                break

        # Activating the loaded topic
        topic_name = self.ALDialog.loadTopic(self.topf_path.encode('utf-8'))
        self.ALDialog.activateTopic(topic_name)
        
        # Starting the dialog engine - we need to type an arbitrary string as the identifier
        # We subscribe only ONCE, regardless of the number of topics we have activated
        self.ALDialog.subscribe('my_dialog_example')
        try:       
            value = raw_input("")
            
        except KeyboardInterrupt:

            stop_flag = True
            # Stop the dialog engine
            self.ALDialog.unsubscribe('my_dialog_example')
            # Deactivate and unload the main topic
            self.ALDialog.deactivateTopic(topic_name)
            self.ALDialog.unloadTopic(topic_name)  

        
