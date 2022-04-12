from pynput import keyboard

def on_press(key):
    try:
        print('↓[{0}]/{1}'.format(key.char, 'alphanumeric'))
    except AttributeError:
        print('↓[{0}]/{1}'.format(key, 'special'))


def on_release(key):
    try:
        print('↑[{0}]/{1}'.format(key.char, 'alphanumeric'))
    except AttributeError:
        print('↑[{0}]/{1}'.format(key, 'special'))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

print(f'Listener started...')
listener.start()
