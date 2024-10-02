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

# normal posture
rp_service = session.service("ALRobotPosture")
posture = "Stand"
speed = 0.7
rp_service.goToPosture(posture,speed)
app.run()

