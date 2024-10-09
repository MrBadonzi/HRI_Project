import os, qi

def onSonar(value):
    print("value")

pip = os.getenv('PEPPER_IP')
pport = 9559
url = "tcp://" + pip + ":" + str(pport)

app = qi.Application(["App", "--qi-url=" + url ])
app.start() # non blocking
session = app.session
memory_service=app.session.service("ALMemory")


# sonar
sonar_service = session.service("ALSonar")
# sl = sonar_service.getSensorList() # vector of sensor names
# print(sl)
# v = sonar_service.getStatus()  # vector of sensor status [name, bool]
# print(v)


# sonar memory keys
sonarValueList = ["Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value",
              	"Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value"]
sonarValues =  memory_service.getListData(sonarValueList)
print(sonarValues) # front, back

anySonar = memory_service.subscriber("SonarRightNothingDetected")
idAnySonar = anySonar.signal.connect(onSonar)
#sonar_service.subscribe("myApp")
# left_sonar_value = memory_service.getData("Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value")
# right_sonar_value = memory_service.getData("Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value")

# Print the sonar values
# print("Front Left Sonar:", left_sonar_value)
# print("Front Right Sonar:", right_sonar_value)

#anySonar = memory_service.subscribeToEvent(onSonar)
#idAnySonar = anySonar.signal.connect(onSonar)

app.run() # blocking
