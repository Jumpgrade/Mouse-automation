import pyautogui
import time
pyautogui.pause = 2.5
pyautogui.FAILSAFE = True

# pyautogui.moveTo(1438, 0, duration=0)
# pyautogui.moveRel(0, 898, duration=0)
# pyautogui.click(x=1197, y=894, clicks=2, interval=1, button='left')

for i in range(100):
    pyautogui.scroll(-50)
    time.sleep(0.1)
    break
