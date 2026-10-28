from pynput import keyboard
import pyautogui
import time


class MyException(Exception):
    pass


def on_press(key):
    print(key)
    if key == keyboard.Key.esc or key == keyboard.Key.esc:
        raise MyException(key)


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()

    except MyException as button:
        pyautogui.pause = 2.5
        pyautogui.FAILSAFE = True

        for i in range(2):
            pyautogui.pause = 2.5
            pyautogui.FAILSAFE = True
            for i in range(100):
                pyautogui.scroll(-50)
                time.sleep(0.1)

        print('{} was pressed'.format(button.args[0]))
