# Raddrizza la testa
# Quando avviene tocco alla testa, fa no con testa e torna alla positzione di default.

import os, qi
#headPitch = testa su (-1.0) e giu (1.0)
#headYaw = testa destra (-1.0) e sinistra (1.0) di pepper
def onTouched(value):
    #print(value)
    motion_service  = session.service("ALMotion")
    jointNames = ["HeadYaw"] #HeadYaw, "HeadPitch"
    angles = [1.0, -1.0] #[1.6, -0.2]
    times  = [3.0, 6.0] #[5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)
    print("Movimento finito. Torno alla default position.")
    jointNames = ["HeadYaw", "HeadPitch"]
    angles = [0.0, 0.0]
    times  = [5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

pip = os.getenv('PEPPER_IP')
pport = 9559
url = "tcp://" + pip + ":" + str(pport)

app = qi.Application(["App", "--qi-url=" + url ])
app.start() # non blocking
session = app.session
memory_service=app.session.service("ALMemory")

#look forward
motion_service  = session.service("ALMotion")
jointNames = ["HeadYaw", "HeadPitch"]
angles = [0.0, 0.0]
times  = [5.0, 5.0]
isAbsolute = True
motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

# touch sensors
touch_service = session.service("ALTouch")
sl = touch_service.getSensorList() # vector of sensor names
print(sl)
v = touch_service.getStatus()  # vector of sensor status [name, bool]
print(v)

# callback function
anyTouch = memory_service.subscriber("TouchChanged")
idAnyTouch = anyTouch.signal.connect(onTouched)


#anyTouch.signal.disconnect(idAnyTouch)
    

app.run() # blocking
