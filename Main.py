from pynput.keyboard import Key, Listener
from keyboard import read_key
from pynput.mouse import Listener as mouseListener
keyLog = []

 
def show(key):
    print('\nYou Entered {0}'.format(key))
    keyLog.append(key)
    
def clicked(x,y, button, pressed):
    if pressed == False: return
    print('\nYou Clicked {0}'.format(button))
    keyLog.append(button)
    
def main():
    listener_keyboard = Listener(on_press=show)
    listener_mouse = mouseListener(on_click=clicked)
    listener_mouse.start()
    listener_keyboard.start()

    # temp solution for running the program
    while True:
        if read_key() == "delete":
            print(keyLog)
            quit()
            
if __name__ == "__main__":
    main()
