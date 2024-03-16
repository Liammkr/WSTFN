import tkinter as tk
import psutil
import os
import sys

def close_other_processes():
    current_pid = os.getpid()
    current_script_name = os.path.basename(__file__)
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if proc.info['pid'] != current_pid and \
           'python' in proc.info['name'].lower() and \
           proc.info['cmdline'] is not None and \
           current_script_name not in proc.info['cmdline'] and \
           'cmd.exe' not in proc.info['name']:
            try:
                os.kill(proc.info['pid'], 9)  # Send SIGKILL signal to terminate the process
            except Exception as e:
                print(f"Error occurred while terminating process {proc.info['pid']}: {e}")
        elif 'cmd.exe' in proc.info['name'].lower():
            try:
                os.kill(proc.info['pid'], 9)  # Send SIGKILL signal to terminate the process
            except Exception as e:
                print(f"Error occurred while terminating cmd.exe process {proc.info['pid']}: {e}")
    sys.exit()

def main():
    root = tk.Tk()
    root.title("WSTFN")  # Set window title

    # Configure the root window background color
    root.configure(bg="#1E1E1E")

    # Define button style
    button_style = {
        "bg": "black",  # Green background color
        "fg": "white",    # White text color
        "font": ("Arial", 14),
        "borderwidth": 0,
        "activebackground": "black",  # Darker green when pressed
        "activeforeground": "white"
    }

    button = tk.Button(root, text="Turn off Bot", command=close_other_processes, **button_style)
    button.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  # Make the button cover the entire window

    root.mainloop()

if __name__ == "__main__":
    main()
