import atexit
import os
import readline

history_path = os.path.expanduser("~/.python_history")

print(f"History path: {history_path}")

try:
    readline.read_history_file(history_path)
    print("History loaded successfully.")
except FileNotFoundError:
    print("History file not found.")

atexit.register(readline.write_history_file, history_path)
