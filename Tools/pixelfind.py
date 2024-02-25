import tkinter as tk
import pyautogui

def get_pixel_color():
    x, y = pyautogui.position()
    pixel_color = pyautogui.pixel(x, y)
    color_label.config(text="Color at ({}, {}): {}".format(x, y, pixel_color))

# Create a tkinter window
root = tk.Tk()
root.title("Pixel Color Checker")

# Create a label to display pixel color
color_label = tk.Label(root, text="")
color_label.pack()

# Create a button to trigger color check
check_button = tk.Button(root, text="Check Pixel Color", command=get_pixel_color)
check_button.pack()

# Run the tkinter event loop
root.mainloop()