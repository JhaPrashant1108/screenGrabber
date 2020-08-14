# from pynput.keyboard import Key, Listener
# import pyautogui
# import time
# from datetime import datetime
# start_time = time.time()
# key_pressed = 0
# def on_press(key):
#     global start_time
#     print('{0} pressed'.format(
#         key))
#     global key_pressed
#     key_pressed = key_pressed + 1
#     if time.time()-start_time > 15:
#         start_time = time.time()
#         image = pyautogui.screenshot()
#         name = 'KeyPressed'+str(key_pressed//2)+'_'+datetime.now().strftime('_%d_%m_%Y_%H_%M_%S')+'.jpeg'
#         image.save(name)
#         key_pressed = 0

# def on_release(key):
#     global start_time
#     print('{0} release'.format(
#         key))
#     global key_pressed
#     key_pressed = key_pressed + 1
#     if time.time()-start_time > 15: 
#         start_time = time.time()
#         image = pyautogui.screenshot()
#         name = 'KeyPressed'+str(key_pressed//2)+'_'+datetime.now().strftime('_%d_%m_%Y_%H_%M_%S')+'.jpeg'
#         image.save(name)
#         key_pressed = 0



# with Listener(
#             on_press=on_press,
#             on_release=on_release) as listener:
#         listener.join()
# import msvcrt
# while True:
#     if msvcrt.kbhit():
#         key_stroke = msvcrt.getch()
#         print(key_stroke)

#asdasdmas,.dasd.,masd.,aashdgvcagsdvhvkhkjhkjkhkjhkjhkjhkjhkjasd
import keyboard

# def caller():
#     return 1
# keyboard.on_press(caller())<aghsdfagsdfgasfdgasfgasfdgasfdgasfdgsadfxasfdgsafdgfgagsdfgasdfgashdghajsdghjahsdjghasjdhgaj
#asdasdasduuuuuuuuuuuuu