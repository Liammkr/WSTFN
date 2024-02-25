import cv2
import pyautogui
import numpy as np
import screeninfo
import time
# Get screen resolution
screen = screeninfo.get_monitors()[0]
width, height = screen.width, screen.height
# Calculate center coordinates
middle_x = width // 2
middle_y = height // 2
print("Center coordinates:", middle_x, middle_y)
def find_and_move_target(target_image):
    # Capture the screen
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    # Load the target image
    target_image = cv2.imread(target_image)
    # Perform template matching
    result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
    # Get the location of the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    bottom_right = (top_left[0] + target_image.shape[1], top_left[1] + target_image.shape[0])
    # Move the mouse to the center of the target image
    global center_y
    global center_x
    center_x = (top_left[0] + bottom_right[0]) // 2 
    center_y = (top_left[1] + bottom_right[1]) // 2
    print(center_x, center_y)
    pyautogui.moveTo(center_x,center_y)
    global xdist
    global ydist
    xdist = abs(center_x-middle_x)
    ydist = abs(center_y-middle_y)
# Path to the target
target_image_path = "test3.png"
print("Press 'k' to initiate search and mouse movement. Press 'q' to quit.")
while True:
    find_and_move_target(target_image_path)
    if xdist > 200:
        if middle_x > center_x:
            pyautogui.keyDown('a')
            time.sleep(0.5)
            pyautogui.keyUp('a')
        if middle_x < center_x:
            pyautogui.keyDown('d')
            time.sleep(0.5)
            pyautogui.keyUp('d')
    if ydist > 200:
        if middle_y < center_y:
            pyautogui.keyDown('s')
            time.sleep(0.5)
            pyautogui.keyUp('s')
        if middle_y > center_y:
            pyautogui.keyDown('w')
            time.sleep(0.5)
            pyautogui.keyUp('w')

