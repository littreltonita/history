from pynput import keyboard

key_history = []

def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)

    key_history.append(key_str)

    print(f": {key_str}")

    if key == keyboard.Key.esc:
        with open("key_history.txt", "w") as file:
            file.write("".join(key_history))
        return False

listener = keyboard.Listener(on_press=on_press)

listener.start()

listener.join()
