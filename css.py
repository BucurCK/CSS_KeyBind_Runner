import time
import pyautogui
import pygetwindow as gw
import argparse
import sys

# Initialize argument parser
parser = argparse.ArgumentParser(description="Run commands with keybinds.")

# Add argument for command
parser.add_argument('command', type=str, help="The command to run (e.g., 'build', 'test', etc.)")

# Parse arguments
args = parser.parse_args()


# Mapping of commands to keybinds
command_map = {
    'build': 'ctrl+b',
    'rebuild': 'ctrl+shift+b',
    'clean': 'ctrl+alt+c',
    'debug': 'f11',
    # Add more commands as needed
}

if args.command == 'help':
	print("--> build: 'ctrl+b'\n--> rebuild: 'ctrl+shift+b'\n--> clean: 'ctrl+alt+c'\n--> debug: 'f11'")
	sys.exit()

# Get the corresponding keybind for the command
keybind = command_map.get(args.command, None)

# Define part of the CSS window title
partial_css_window_title = "Code Composer Studio"

# Get the currently active window (should be VS Code)
initial_window = gw.getActiveWindow()

# Function to find a window by a partial title match
def find_window(partial_title):
    for window in gw.getAllWindows():
        if partial_title.lower() in window.title.lower():
            return window
    return None

# Find the CSS window
css_window = find_window(partial_css_window_title)

if css_window:
	# Switch to CSS
	css_window.activate()
	time.sleep(1)

	# If a keybind is found, split and use pyautogui.hotkey()
	if keybind:
		# Split the keybind by '+' to separate modifiers and the main key
		keys = keybind.split('+')
		print(f"Pressing the keybind: {keybind}")
		pyautogui.hotkey(*keys)  # Unpack the list and pass to pyautogui.hotkey()
	else:
		print(f"Unknown command: {args.command}. Available commands are {', '.join(command_map.keys())}.")
		time.sleep(1)

    # Switch back to the original VS Code window
	if initial_window:
		initial_window.activate()
	else:
		print("Couldn't switch back to VS Code.")
            
else:
    print("CSS window not found.")
