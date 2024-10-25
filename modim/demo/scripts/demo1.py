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

    action = im.ask('welcome')  # wait for button
    # im.ask("menu")

    if action == 'Menu':
        im.display.loadUrl('menu.html')
        menu = im.ask('menu')
        if menu == 'yes':
            # display answer
            im.executeModality('text_default', 'vongole e bottarga')
            # Using TTS service of the robot to speak
            im.executeModality('TTS', 'vongole e bottarga')
            time.sleep(5)
        if menu == 'no':
            im.executeModality('text_default', 'okay stupido')
            # Using TTS service of the robot to speak
            im.executeModality('TTS', 'okay stupido')
            time.sleep(5)

        prenotare = im.ask('prenotare')

        if prenotare!='timeout':
            im.display.loadUrl('reservations.html')

            time.sleep(1)
            # TODO: CHIDERE SE HANNO PRENOTAZIONE
            tavolo = im.ask('reservation')

            if int(tavolo) <= 4:
                im.ask('indicazioni')
                time.sleep(5)
                im.init()

            elif int(tavolo) > 4:
                im.ask('occupato')
                im.ask('goodbye')
                im.init()

            else:
                im.ask('goodbye')
                im.init()


        else:
            im.ask('goodbye')
            im.init()

    elif action=='Tables':
        # TODO: CHIDERE SE HANNO PRENOTAZIONE
        im.display.loadUrl('reservations.html')
        time.sleep(1)
        tavolo = im.ask('reservation')

        if int(tavolo)<=4:
            im.ask('indicazioni')
            time.sleep(5)
            im.init()

        elif int(tavolo)>4:
            im.ask('occupato')
            im.ask('goodbye')
            im.init()

        else:
            im.ask('goodbye')
            im.init()


    elif action=='timeout':
        im.ask('goodbye')
        im.init()


if __name__ == "__main__":
    mws = ModimWSClient()

    # local execution
    mws.setDemoPathAuto(__file__)
    # remote execution
    # mws.setDemoPath('<ABSOLUTE_DEMO_PATH_ON_REMOTE_SERVER>')

    mws.run_interaction(i1)
