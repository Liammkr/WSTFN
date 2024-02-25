# main.py

import subprocess
import platform

def start_other_script():
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["start", "cmd", "/k", "python", "image.py"], shell=True)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "Terminal", "python", "image.py"])
        elif platform.system() == "Linux":
            subprocess.Popen(["x-terminal-emulator", "-e", "python", "image.py"])
        else:
            print("Unsupported platform:", platform.system())
    except Exception as e:
        print("Error starting image.py:", e)

if __name__ == "__main__":
    start_other_script()
