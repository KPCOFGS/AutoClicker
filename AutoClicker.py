import time
import pyautogui
from pynput import keyboard
import argparse

def on_press(key):
    global start
    global loop
    if key == keyboard.Key.delete:
        print("Exiting program...")
        loop = False
        return False
    try:
        if key.char == args.start_key and start == 0:
            start = 1
        elif key.char == args.start_key and start == 1:
            start = 0
    except AttributeError:
        pass

def on_release(key):
    pass

parser = argparse.ArgumentParser(description='Auto Clicker with pynput')
parser.add_argument('start_key', type=str, help='Key to start and stop clicking')
parser.add_argument('interval', type=float, help='Time interval between clicks')
parser.add_argument('mouse', type=str, help='Left or right mouse click')
args = parser.parse_args()
interval = args.interval
which_mouse = args.mouse.lower()
print(f"Press '{args.start_key}' to start and stop clicking")
print("Press 'Delete' key to exit the program.")
loop = True
start = 0

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
if which_mouse == "left":
    while loop:
        if start == 1:
            pyautogui.click()
            time.sleep(interval)
        else:
            time.sleep(0.1)
elif which_mouse == "right":
    while loop:
        if start == 1:
            pyautogui.click(button='right')
            time.sleep(interval)
        else:
            time.sleep(0.1)
