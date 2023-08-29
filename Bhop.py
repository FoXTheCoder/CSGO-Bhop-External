import keyboard  # Library for working with keyboard input
import win32gui  # Library for interacting with the Windows GUI
from colorama import Fore, init  # Library for colored console output
import os  # Library for interacting with the operating system
import time  # Library for working with time intervals

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")  # Clear the console

init()
clear_console()  # Clear the console screen
print(f"[{Fore.BLUE}INFO{Fore.RESET}] Started ShadowHop.")  # Print an info message

def main():
    while True:  # Infinite loop
        active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())  # Get the title of the active window
        
        if not active_window.startswith("Counter-Strike: Global Offensive"):  # Check if the active window is not CS:GO
            continue  # Skip the rest of the loop and go to the next iteration

        if keyboard.is_pressed("space"):  # Check if the space key is pressed
            keyboard.write('space')  # Simulate typing the 'space' key
            time.sleep(0.07)  # Pause for a short interval (time between jumps)
            continue  # Skip the rest of the loop and go to the next iteration

        time.sleep(0.02)  # Pause for a short interval

if __name__ == '__main__':
    main()  # Call the main function if the script is run directly
