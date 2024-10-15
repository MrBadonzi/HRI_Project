import os, sys

pdir = os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pdir+ '/cmd_server')
import pepper_cmd
from pepper_cmd import *

begin() # connect to robot/simulator with IP in PEPPER_IP env variable

# see pepper_tools/cmd_server/pepper_cmd.py
pepper_cmd.robot.startSensorMonitor()


# wait until front sonar detect something (range < 1.0)
personHere = False
while not personHere:
  p = pepper_cmd.robot.sensorvalue()
  personHere = p[1]<1.0 and  p[1]!=0  # front sonar
  print(p)

# speech synthesis
if personHere == True: 
   pepper_cmd.robot.say("Hello. How are you?")

pepper_cmd.robot.stopSensorMonitor()


end()
