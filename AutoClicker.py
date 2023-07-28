import keyboard
import time
import mouse
class AutoClick():
    def __init__(self,key_1, key_2):
        start = 0
        self.key_1 = key_1
        self.key_2 = key_2
        while True:
            if keyboard.is_pressed(key_1):
                start = 1
            elif keyboard.is_pressed(key_2):
                start = 0
            if start == 1:
                mouse.click()
            time.sleep(0.1)
