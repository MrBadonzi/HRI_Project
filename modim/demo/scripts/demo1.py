import sys
import time
import os
import random

try:
    sys.path.insert(0, os.getenv('MODIM_HOME') + '/src/GUI')
except Exception as e:
    print
    "Please set MODIM_HOME environment variable to MODIM folder."
    sys.exit(1)

# Set MODIM_IP to connnect to remote MODIM server

import ws_client
from ws_client import *


def i1():
    im.display.loadUrl('index.html')

    im.init()

    a = im.ask('welcome')  # wait for button
    # im.ask("menu")

    if a == 'Menu':
        im.display.loadUrl('menu.html')
        a = im.ask('menu')
        if a == 'yes':
            # display answer
            im.executeModality('text_default', 'vongole e bottarga')
            # Using TTS service of the robot to speak
            im.executeModality('TTS', 'vongole e bottarga')
        else:
            im.executeModality('text_default', 'okay stupido')
            # Using TTS service of the robot to speak
            im.executeModality('TTS', 'okay stupido')
            #time.sleep(1000)

    elif a=='timeout':
        im.init()


if __name__ == "__main__":
    mws = ModimWSClient()

    # local execution
    mws.setDemoPathAuto(__file__)
    # remote execution
    # mws.setDemoPath('<ABSOLUTE_DEMO_PATH_ON_REMOTE_SERVER>')

    mws.run_interaction(i1)
