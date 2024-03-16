import pyautogui
import time
from dhooks import Webhook , File
gg = Webhook('https://discord.com/api/webhooks/1210688142496235640/3qnfG6w2x5MjMFQnW0cGXJBhD4YjW0FGPc7awIKAqz9nARafBucS-S1rwILLHiirx1Tr')
# Define the coordinates you want to check
# Open the file and pass the file object
file = File('screenshots/screenshot_1.png', name='cat.png')  # optional name for discord


# Define the boundaries of the area (top-left and bottom-right coordinates)
x1 = 775
y1 = 135
x2 = 875
y2 = 185

# Define the RGB values of the color you want to check
desired_color = (255, 255, 255)  # Red color, change this to the desired color


# Iterate over the pixels in the screenshot

while True:
    # Take a screenshot of the specified area
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

    # Iterate over the pixels in the screenshot
    for x in range(x2 - x1):
        for y in range(y2 - y1):
            # Get the color of the pixel at the current coordinates
            pixel_color = screenshot.getpixel((x, y))

            # Check if the pixel color matches the desired color
            if pixel_color == desired_color:
                print("Pixel at ({}, {}) is the desired color.".format(x + x1, y + y1))
                gg.send("hi")
            else:
                print("Pixel at ({}, {}) is not the desired color. Color was: {}".format(x + x1, y + y1, pixel_color))

    # Add a delay before the next iteration
    # You can adjust the sleep time as needed
    time.sleep(1)