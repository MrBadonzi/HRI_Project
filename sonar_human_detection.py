import os, sys

pdir = os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pdir+ '/cmd_server')
import pepper_cmd
from pepper_cmd import *
def sonar_detection():
    p = pepper_cmd.robot.sensorvalue()
    personHere = p[1]<1.0 and  p[1]!=0  # front sonar
    return personHere