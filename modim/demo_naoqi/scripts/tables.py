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
    im.display.loadUrl('reservations_naoqi.html')
    time.sleep(100)
    im.init()




if __name__ == "__main__":
    mws = ModimWSClient()

    # local execution
    mws.setDemoPathAuto(__file__)
    # remote execution
    #mws.setDemoPath('10.0.1.200')

    mws.run_interaction(i1)
