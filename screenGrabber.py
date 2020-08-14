import pyautogui
import time
from datetime import datetime

user = 'prashantJha'

while True:
    image = pyautogui.screenshot()
    datetimeset = str(datetime.now()).split(" ")
    name = user+'_'+datetime.now().strftime('_%d_%m_%Y_%H_%M_%S')+'.jpeg'
    image.save(name)
    time.sleep(300)