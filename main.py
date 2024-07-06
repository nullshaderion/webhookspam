import requests
from pystyle import Colorate,Colors,Write
import time

text = '''


██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ ██║██║╚██╗██║██║   ██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                 


'''

print(Colorate.Vertical(Colors.blue_to_purple, text))

while True:
    try:
        counter = 0
        webhook_url = str(input('Input URL: '))
        message = str(input('Input Message: '))
        user = str(input('Optional: input username: '))
        timeout = int(input('Timeout (for ratelimit): '))
        Numofspam = int(input('Number of times to spam: '))
        if user == "":
            user = "Default"



        data = {
        "username": user,
        "content": message
        }

        while True:
                r = requests.post(webhook_url, json=data)
                counter = counter + 1
                if counter == Numofspam:
                        break
                time.sleep(timeout)
                if timeout == None:
                    time.sleep(0)
                r.raise_for_status()

    except requests.exceptions.MissingSchema as e:
        print('it has to be a valid webhook dawg')
    except ValueError as e:
        print('a fucking number you dumbass')
    except requests.exceptions.HTTPError as e:
        print(f'error with http, error: {e} ')
