import os, qi

pip = os.getenv('PEPPER_IP')
pport = 9559
url = "tcp://" + pip + ":" + str(pport)

app = qi.Application(["App", "--qi-url=" + url ])
app.start() # non blocking
session = app.session
memory_service=app.session.service("ALMemory")

# # voice only
# tts_service = session.service("ALTextToSpeech")
# tts_service.setLanguage("English")
# tts_service.setParameter("speed", 90)
# tts_service.say("Hello. How are you?")

# voice and gestures
ans_service = session.service("ALAnimatedSpeech")
configuration = {"bodyLanguageMode":"contextual"}
ans_service.say("Hello. How are you?", configuration)

# try:
    
#     tabletService = session.service("ALTabletService")

#     # Don't forget to disconnect the signal at the end
#     signalID = 0

#     # function called when the signal onTouchDown is triggered
#     def callback(x, y):
#         print("coordinate are x: ", x, " y: ", y)
#         if x > 640:
#             # disconnect the signal
#             tabletService.onTouchDown.disconnect(signalID)
#             app.stop()

#     # attach the callback function to onJSEvent signal
#     signalID = tabletService.onTouchDown.connect(callback)
#     #app.run()

# except Exception, e:
#     print("Error was: ", e)

# normal posture
#rp_service = session.service("ALRobotPosture")
#posture = "Stand"
#speed = 0.7
#rp_service.goToPosture(posture,speed)
app.run()

