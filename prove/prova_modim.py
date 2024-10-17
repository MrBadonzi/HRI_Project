import os, sys

pdir = os.getenv('MODIM_HOME')
sys.path.append(pdir + '/src/GUI')

import sys
import time
import os
import random

try:
    sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
    print ("Please set MODIM_HOME environment variable to MODIM folder.")
    sys.exit(1)

# Set MODIM_IP to connnect to remote MODIM server

import ws_client
from ws_client import *

def i1():

    im.init()

    im.display.loadUrl('index.html')

    # Setting HTML element of the web page
    im.executeModality('text_title','HRI 2020')
    im.executeModality('text_default','Hello!')
    im.executeModality('image_default','img/dolphin.jpg')

    # show buttons
    im.display.remove_buttons()
    im.executeModality('BUTTONS',[['yes','Yes'],['no','No']])

    # set ASR
    im.executeModality('ASR',['yes','no'])

    # wait for answer
    a = im.ask(actionname=None, timeout=10)

    # display answer
    im.executeModality('TEXT_default',a)


    # Using TTS service of the robot to speak
    im.executeModality('TTS','Congratulations for your first MODIM program')





    im.init()




mws = ModimWSClient()

# local execution
mws.setDemoPathAuto(__file__)
# remote execution
# mws.setDemoPath('<ABSOLUTE_DEMO_PATH_ON_REMOTE_SERVER>')

mws.run_interaction(i1)






