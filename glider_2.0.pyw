import pyautogui
import time
import screeninfo
import multiprocessing
t=0
m=0.5
i=0.25
screen = screeninfo.get_monitors()[0]
width, height = screen.width, screen.height
middle_x = width // 2
middle_y = height // 2

# Locate the image on the screen
def find_image(image_path):
    try:
        position = pyautogui.locateOnScreen(image_path, confidence=0.65)
        if position is not None:
            return position.left, position.top
        else:
            return None, None
    except Exception as e:
        print("Error:", e)
        return None, None

# Main loop
def main(image_path):
    while True:
        for img_path in image_path:
            x, y = find_image(img_path)
            with open("var.txt", "r") as file:
                    variable_received = file.read()
            #print("Variable received:", variable_received)
            if variable_received == 'False':
                if x is not None and y is not None:
                    print("Image found at position: (x={}, y={})".format(x, y))
                    # Add your desired action here, for example, click on the image
                    xdist = abs(x-middle_x)
                    ydist = abs(y-middle_y)
                    if middle_x > x:
                            pyautogui.keyDown('a')
                            time.sleep(0.005*xdist/(t*m))
                            pyautogui.keyUp('a')
                    if middle_x < x:
                            pyautogui.keyDown('d')
                            time.sleep(0.005*xdist/(t*m))
                            pyautogui.keyUp('d')
                    if middle_y < y:
                            pyautogui.keyDown('s')
                            time.sleep(0.005*ydist/(t*m))
                            pyautogui.keyUp('s')
                    if middle_y > y:
                            pyautogui.keyDown('w')
                            time.sleep(0.005*ydist/(t*m))
                            pyautogui.keyUp('w')    
                    t+=i
                else:
                    print("Image not found on the screen.")
                    t+=i
            else:
                print("landed")
                t=0.25

# Function to run main loop in a separate process
def run_main(image_path):
    process = multiprocessing.Process(target=main, args=(image_path,))
    process.start()

# Example usage
if __name__ == "__main__":
    image_path = ['Images/marker.png', 'Images/marker2.png', 'Images/Marker3.png', 'Images/marker4.png', 'Images/marker5.png', 'Images/Marker6.png','Images/marker7.png','Images/marker8.png','Images/marker9.png']  # Set image path
    run_main(image_path)