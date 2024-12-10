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
    # im.ask("PiattodelGiorno")

    # VUOLE VEDERE MENU
    if action == 'Menu':

        im.display.loadUrl('menu.html')

        # VUOLE VEDERE PIATTO DEL GIORNO
        menu = im.ask('PiattodelGiorno')
        if menu == 'yes':
            # display answer
            im.executeModality('text_default', 'Spaghetti with clamps and bottarga')
            # Using TTS service of the robot to speak
            im.executeModality('TTS', 'Spaghetti with clamps and bottarga')
            time.sleep(5)

        # SI VUOLE SEDERE AL TAVOLO?
        prenotare = im.ask('sedere')

        # SI
        if prenotare != 'timeout':

            im.display.loadUrl('reservations.html')

            time.sleep(1)

            # HA PRENOTATO?
            prenotazione = im.ask('prenotato')
            if prenotazione == 'no':
                # QUANTI SIETE?
                tavolo = im.ask('postiTavolo')

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
                nome = im.ask('nome')
                #im.ask('indicazioni')
                if nome == "none":
                    im.ask('mismatch')
                    time.sleep(5)
                    im.init()
                else:
                    im.ask('indicazioni')
                    time.sleep(5)
                    im.init()




        else:
            im.ask('goodbye')
            im.init()

    # VOGLIO SEDERMI AL TAVOLO
    elif action == 'Tables':

        im.display.loadUrl('reservations.html')
        time.sleep(1)
        # AVETE PRENOTATO?
        prenotazione = im.ask('prenotato')
        if prenotazione == 'no':
            # QUANTI SIETE?
            tavolo = im.ask('postiTavolo')

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
            nome = im.ask('nome')
            #im.ask('indicazioni')
            if nome == "none":
                im.ask('mismatch')
                time.sleep(5)
                im.init()
            else:
                im.ask('indicazioni')
                time.sleep(5)
                im.init()


    elif action == 'timeout':
        time.sleep(100)
        im.ask('goodbye')
        im.init()




if __name__ == "__main__":
    mws = ModimWSClient()

    # local execution
    mws.setDemoPathAuto(__file__)
    # remote execution
    #mws.setDemoPath('10.0.1.200')

    mws.run_interaction(i1)
