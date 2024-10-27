def tablet_motion(session, tts_service):
    angles_tablet = {"RElbowRoll": 1.55, "RElbowYaw": 1.01, "RHand": 1, "RShoulderPitch": 0.97, "RShoulderRoll": -0.65, "RWristYaw": 1.20,
                    "LElbowRoll": -0.01, "LElbowYaw": -2.07, "LHand": 1, "LShoulderPitch": 1.38, "LShoulderRoll": 1.56, "LWristYaw": -0.84}
    
    angles_reset = {"RElbowRoll": 0.0, "RElbowYaw": 1.0, "RHand": 0, "RShoulderPitch": 1.49, "RShoulderRoll": 0.05, "RWristYaw": 1.19,
                    "LElbowRoll": 0.0, "LElbowYaw": -1.0, "LHand": 0, "LShoulderPitch": 1.49, "LShoulderRoll": 0.07, "LWristYaw": -0.84}
    
    motion_service  = session.service("ALMotion")
    jointNames = ["RElbowRoll", "RElbowYaw", "RHand", "RShoulderPitch", "RShoulderRoll", "RWristYaw", 
                  "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch", "LShoulderRoll", "LWristYaw"]
    angles = [1.55, 1.01, 1, 0.97, -0.65, 1.20,
             -0.01, -2.07, 1, 1.38, 1.56, -0.84]
    times  = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
             5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    tts_service.say("The table displayed on the screen is ready for you, please take your seat.")
    #print("Resetting\n")

    motion_service  = session.service("ALMotion")
    jointNames = ["RElbowRoll", "RElbowYaw", "RHand", "RShoulderPitch", "RShoulderRoll", "RWristYaw",
                  "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch", "LShoulderRoll", "LWristYaw"]
    angles = [0.0, 1.0, 0.0, 1.49, 0.05, 1.19,
              0.0, -1.0, 0, 1.49, 0.07, -0.84]
    times  = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
              5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

def sad_motion(session, tts_service ,table = False, reservation = False):
    audio_service = session.service("ALAudioPlayer")
    audio_service.playFile("/sounds/bad.mp3", _async=True)


    angles_sad = {"RElbowRoll": 1.43, "RElbowYaw": 0.17, "RHand": 0, "RShoulderPitch": 2.08, "RShoulderRoll": -0.76, "RWristYaw": -0.04,
                    "LElbowRoll": -1.37, "LElbowYaw": 0.37, "LHand": 0, "LShoulderPitch": 1.77, "LShoulderRoll": 0.72, "LWristYaw": 0.04,
                    "HeadPitch": 0.28}
    
    angles_reset = {"RElbowRoll": 0.0, "RElbowYaw": 1.0, "RHand": 0, "RShoulderPitch": 1.49, "RShoulderRoll": 0.05, "RWristYaw": 1.19,
                    "LElbowRoll": 0.0, "LElbowYaw": -1.0, "LHand": 0, "LShoulderPitch": 1.49, "LShoulderRoll": 0.07, "LWristYaw": -0.84,
                    "HeadPitch": -0.38, "HeadYaw": 0.01}
    
    motion_service  = session.service("ALMotion")
    jointNames = ["RElbowRoll", "RElbowYaw", "RHand", "RShoulderPitch", "RShoulderRoll", "RWristYaw", 
                  "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch", "LShoulderRoll", "LWristYaw",
                  "HeadPitch"]
    angles = [angles_sad["RElbowRoll"], angles_sad["RElbowYaw"], angles_sad["RHand"], angles_sad["RShoulderPitch"], angles_sad["RShoulderRoll"], angles_sad["RWristYaw"], 
              angles_sad["LElbowRoll"], angles_sad["LElbowYaw"], angles_sad["LHand"], angles_sad["LShoulderPitch"], angles_sad["LShoulderRoll"], angles_sad["LWristYaw"],
              angles_sad["HeadPitch"]]
    times  = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
             5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
             5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)
    #, "HeadYaw": -0.66
    jointNames = ["HeadYaw"]
    angles = [1.0, -1.0] 
    times  = [2.0, 4.0] 
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)
    if(table):
        tts_service.say("I'm sorry, there are no available tables.")
    elif(reservation):
        tts_service.say("I don't have any reservation with that name. I will contact someone")
    
    print("Resetting\n")

    motion_service  = session.service("ALMotion")
    jointNames = ["RElbowRoll", "RElbowYaw", "RHand", "RShoulderPitch", "RShoulderRoll", "RWristYaw",
                  "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch", "LShoulderRoll", "LWristYaw",
                  "HeadPitch", "HeadYaw"]
    angles = [0.0, 1.0, 0.0, 1.49, 0.05, 1.19,
              0.0, -1.0, 0, 1.49, 0.07, -0.84,
              -0.38, 0.01]
    times  = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
              5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
              5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)


def happy_motion(session):
    audio_service = session.service("ALAudioPlayer")
    audio_service.playFile("/sounds/happy.mp3", _async=True)

    angles_happy = {"RElbowRoll": 1.36, "RElbowYaw": 0.37, "RHand": 0, "RShoulderPitch": -0.99, "RShoulderRoll": -0.99, "RWristYaw": 1.82,
                    "LElbowRoll": -1.31, "LElbowYaw": -0.37, "LHand": 0, "LShoulderPitch": -1.01, "LShoulderRoll": 1.12, "LWristYaw": -1.49}
    
    angles_reset = {"RElbowRoll": 0.0, "RElbowYaw": 1.0, "RHand": 0, "RShoulderPitch": 1.49, "RShoulderRoll": 0.05, "RWristYaw": 1.19,
                    "LElbowRoll": 0.0, "LElbowYaw": -1.0, "LHand": 0, "LShoulderPitch": 1.49, "LShoulderRoll": 0.07, "LWristYaw": -0.84,
                    "HeadPitch": -0.38, "HeadYaw": 0.01}
    
    motion_service  = session.service("ALMotion")
    jointNames = ["RElbowRoll", "RElbowYaw", "RHand", "RShoulderPitch", "RShoulderRoll", "RWristYaw", 
                  "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch", "LShoulderRoll", "LWristYaw"]
    angles = [angles_happy["RElbowRoll"], angles_happy["RElbowYaw"], angles_happy["RHand"], angles_happy["RShoulderPitch"], angles_happy["RShoulderRoll"], angles_happy["RWristYaw"], 
              angles_happy["LElbowRoll"], angles_happy["LElbowYaw"], angles_happy["LHand"], angles_happy["LShoulderPitch"], angles_happy["LShoulderRoll"], angles_happy["LWristYaw"]]
    times  = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
             5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    
    for i in range(5):
            jointNames = ["RElbowRoll", "LElbowRoll", "HipRoll", "HeadPitch"]
            angles = [0.68, -1.5, -0.23, 1]
            times  = [0.8, 0.8, 0.8, 0.8]
            isAbsolute = True
            motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

            jointNames = ["RElbowRoll", "LElbowRoll", "HipRoll", "HeadPitch"]
            angles = [1.36, -1.0, 0.23, -1]
            times  = [0.8, 0.8, 0.8, 0.8]
            isAbsolute = True
            motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    
    print("Resetting\n")

    motion_service  = session.service("ALMotion")
    jointNames = ["RElbowRoll", "RElbowYaw", "RHand", "RShoulderPitch", "RShoulderRoll", "RWristYaw",
                  "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch", "LShoulderRoll", "LWristYaw",
                  "HeadPitch", "HeadYaw", "HipRoll"]
    angles = [0.0, 1.0, 0.0, 1.49, 0.05, 1.19,
              0.0, -1.0, 0, 1.49, 0.07, -0.84,
              -0.38, 0.01, 0.0]
    times  = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
              5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
              5.0, 5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)



def neutral_motion(session):
    audio_service = session.service("ALAudioPlayer")
    audio_service.playFile("/sounds/neutral.mp3", _async=True)

    angles_neutral = {"RElbowRoll": 1.56, "RElbowYaw": 0.95, "RHand": 1, "RShoulderPitch": 1.67, "RShoulderRoll": -0.53, "RWristYaw": 1.53,
                    "LElbowRoll": -1.28, "LElbowYaw": -1.56, "LHand": 1, "LShoulderPitch": 0.25, "LShoulderRoll": 1.13, "LWristYaw": 0.04}
    
    angles_reset = {"RElbowRoll": 0.0, "RElbowYaw": 1.0, "RHand": 0, "RShoulderPitch": 1.49, "RShoulderRoll": 0.05, "RWristYaw": 1.19,
                    "LElbowRoll": 0.0, "LElbowYaw": -1.0, "LHand": 0, "LShoulderPitch": 1.49, "LShoulderRoll": 0.07, "LWristYaw": -0.84,
                    "HeadPitch": -0.38, "HeadYaw": 0.01}
    
    motion_service  = session.service("ALMotion")
    jointNames = ["RElbowRoll", "RElbowYaw", "RHand", "RShoulderPitch", "RShoulderRoll", "RWristYaw", 
                  "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch", "LShoulderRoll", "LWristYaw"]
    angles = [angles_neutral["RElbowRoll"], angles_neutral["RElbowYaw"], angles_neutral["RHand"], angles_neutral["RShoulderPitch"], angles_neutral["RShoulderRoll"], angles_neutral["RWristYaw"], 
              angles_neutral["LElbowRoll"], angles_neutral["LElbowYaw"], angles_neutral["LHand"], angles_neutral["LShoulderPitch"], angles_neutral["LShoulderRoll"], angles_neutral["LWristYaw"]]
    times  = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
             5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    for i in range(2):
        jointNames = ["LElbowRoll"]
        angles = [-1.57, -0.87] 
        times  = [2.0, 4.0] 
        isAbsolute = True
        motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    
    print("Resetting\n")

    motion_service  = session.service("ALMotion")
    jointNames = ["RElbowRoll", "RElbowYaw", "RHand", "RShoulderPitch", "RShoulderRoll", "RWristYaw",
                  "LElbowRoll", "LElbowYaw", "LHand", "LShoulderPitch", "LShoulderRoll", "LWristYaw",
                  "HeadPitch", "HeadYaw", "HipRoll"]
    angles = [0.0, 1.0, 0.0, 1.49, 0.05, 1.19,
              0.0, -1.0, 0, 1.49, 0.07, -0.84,
              -0.38, 0.01, 0.0]
    times  = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
              5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
              5.0, 5.0, 5.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)