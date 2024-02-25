import pyautogui
import cv2
import numpy as np

# Get screen resolution
screen_width, screen_height = pyautogui.size()

# Set coordinates
x = 1300
y = 120
box_width = 1200
box_height = 10000

# Main loop
while True:
    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Convert screenshot to numpy array
    frame = np.array(screenshot)

    # Draw the box
    cv2.rectangle(frame, (x, y), (x + box_width, y + box_height), (0, 255, 0), 2)

    # Show the image
    cv2.imshow("Overlay", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all windows
cv2.destroyAllWindows()
