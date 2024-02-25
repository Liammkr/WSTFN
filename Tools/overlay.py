import os
import pyautogui
from PIL import Image
import time
time.sleep(2)

# Create screenshots directory if it doesn't exist
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Get the number of existing screenshots
existing_screenshots = len([name for name in os.listdir('screenshots') if os.path.isfile(os.path.join('screenshots', name))])

# Define the coordinates of the area you want to capture
x1, y1, x2, y2 = 1300, 20, 2500, 2120  # Change these values as per your requirement

# Take screenshot
screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

# Save screenshot with an increasing number
screenshot_path = f'screenshots/screenshot_{existing_screenshots + 1}.png'
screenshot.save(screenshot_path)
print(screenshot_path)
