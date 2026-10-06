from pynput import keyboard


class MyException(Exception):
    pass


def on_press(key):
    if key == keyboard.Key.esc:
        raise MyException(key)


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{} was pressed'.format(e.args[0]))
