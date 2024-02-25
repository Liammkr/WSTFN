import time
import pyautogui
def is_doors_present(text):
    return "READY" in text.lower()

# Main loop
while True:
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to grayscale
    grayscale_image = screenshot.convert('L')
    
    # Get the width and height of the image
    width, height = grayscale_image.size
    
    # Define the region where you want to search for the word "doors"
    search_region = (0, 0, width, height)
    
    # Search for the word "doors" in the region
    found_doors = pyautogui.locateOnScreen('Readyup.png', grayscale=True, region=search_region)
    
    # Check if "doors" is found
    if found_doors:
        print("Ready Up found at:", found_doors)
        break  # Exit the loop if the word "doors" is found
    print("Not Found")
    # Wait for a short duration before taking the next screenshot
    # You can adjust the duration as needed