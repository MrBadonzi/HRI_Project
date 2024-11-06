class Sonar:
    def __init__(self, memory_service):
        self.sonarValueList = ["Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value",
                               "Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value"]
        self.memory_service = memory_service

    def getData(self):
        return self.memory_service.getListData(self.sonarValueList)

    def peopleDetection(self, threshold=1.0):
        people_detected = False
        while not people_detected:
            sonarValues = self.getData()
            if (sonarValues[0] != 0.0 and sonarValues[0] <= threshold):  # NO controllo dietro perche accostato a muro
                print(sonarValues)
                people_detected = True
        return people_detected

    def check_people_detection(self, threshold = 1.0):
        sonarValues = self.getData()
        print(sonarValues)
        if (sonarValues[0] != 0.0 and sonarValues[0] <= threshold):  # NO controllo dietro perche accostato a muro
            print(sonarValues)
            people_detected = True
        return people_detected
