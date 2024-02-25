import time
import pyautogui
import random
import time
import pydirectinput
import screeninfo
import cv2
import numpy as np
from dhooks import Webhook , File
import os
import pyautogui
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import subprocess
import platform
def start_other_script():
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["start", "cmd", "/k", "python", "screenshotbutton.py"], shell=True)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "Terminal", "python", "screenshotbutton.py"])
        elif platform.system() == "Linux":
            subprocess.Popen(["x-terminal-emulator", "-e", "python", "screenshotbutton.py"])
        else:
            print("Unsupported platform:", platform.system())
    except Exception as e:
        print("Error starting screenshotbutton.py:", e)
if __name__ == "__main__":
    start_other_script()
cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': str('')
})
ref = db.reference('/WSTFN')
while True:
    hook = Webhook('')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Waiting for match to start'
    print(status)
    ref.update({
        'status' : status
    })
    def is_doors_present(text):
        return "doors" in text.lower()
    while True:
        screenshot = pyautogui.screenshot()
        grayscale_image = screenshot.convert('L')
        width, height = grayscale_image.size
        search_region = (0, 0, width, height)
        found_doors = pyautogui.locateOnScreen('Images/doors.png', grayscale=True, region=search_region)
        if found_doors:
            status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Match Started'
            print(status)
            ref.update({
                'status' : status
            })
            break
        time.sleep(1)
    pyautogui.press('7')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Closed Augments'
    print(status)
    ref.update({
        'status' : status
    })
    pyautogui.press('m')
    time.sleep(0.5)
    pyautogui.click(2012,1210)
    pyautogui.press('m')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Pinged Drop'
    print(status)
    ref.update({
        'status' : status
    })
    time.sleep(random.randint(16,17))
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Jumped From Bus'
    print(status)
    ref.update({
        'status' : status
    })
    time.sleep(random.randint(0,1))
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Deployed Glider'
    print(status)
    ref.update({
        'status' : status
    })
    i =10
    while i > 0:
        pydirectinput.moveRel(0, random.randint(-10000,-9000), relative=True)
        i-=1
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Positioned Camera At Floor'
    print(status)
    ref.update({
        'status' : status
    })
    screen = screeninfo.get_monitors()[0]
    width, height = screen.width, screen.height
    middle_x = width // 2
    middle_y = height // 2
    def find_and_move_target(target_image):
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        target_image = cv2.imread(target_image)
        result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        bottom_right = (top_left[0] + target_image.shape[1], top_left[1] + target_image.shape[0])
        global center_y
        global center_x
        center_x = (top_left[0] + bottom_right[0]) // 2 
        center_y = (top_left[1] + bottom_right[1]) // 2
        global xdist
        global ydist
        xdist = abs(center_x-middle_x)
        ydist = abs(center_y-middle_y)
    target_image_path = "Images/marker.png"
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Gliding To Marker'
    print(status)
    ref.update({
        'status' : status
    })
    while True:
        x1 = 775
        y1 = 135
        x2 = 875
        y2 = 185
        desired_color = (255, 255, 255)
        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        for x in range(x2 - x1):
            for y in range(y2 - y1):
                pixel_color = screenshot.getpixel((x, y))
                if pixel_color == desired_color:
                    break 
            else:
                continue 
            break
        if pixel_color == desired_color:
            status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Landed On Floor'
            print(status)
            ref.update({
                'status' : status
            })
            break
        find_and_move_target(target_image_path)
        if xdist > 250:
            if middle_x > center_x:
                pyautogui.keyDown('a')
                time.sleep(0.5)
                pyautogui.keyUp('a')
            if middle_x < center_x:
                pyautogui.keyDown('d')
                time.sleep(0.5)
                pyautogui.keyUp('d')
        if ydist > 250:
            if middle_y < center_y:
                pyautogui.keyDown('s')
                time.sleep(0.5)
                pyautogui.keyUp('s')
            if middle_y > center_y:
                pyautogui.keyDown('w')
                time.sleep(0.5)
                pyautogui.keyUp('w')
    pyautogui.press('ctrl')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Crouched'
    print(status)
    ref.update({
        'status' : status
    })
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Waiting To Be Eliminated'
    print(status)
    ref.update({
        'status' : status
    })
    def is_doors_present(text):
        return "READY" in text.lower()
    while True:
        screenshot = pyautogui.screenshot()
        grayscale_image = screenshot.convert('L')
        width, height = grayscale_image.size
        search_region = (0, 0, width, height)
        found_ready = pyautogui.locateOnScreen('Images/Readyup.png', grayscale=True, region=search_region)
        if found_ready:
            status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Eliminated'
            print(status)
            ref.update({
                'status' : status
            })
            break 
        time.sleep(5)
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    existing_screenshots = len([name for name in os.listdir('screenshots') if os.path.isfile(os.path.join('screenshots', name))])
    x1, y1, x2, y2 = 1300, 20, 2500, 2120
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Screenshot Taken'
    print(status)
    ref.update({
        'status' : status
    })
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    screenshot_path = f'screenshots/screenshot_{existing_screenshots + 1}.png'
    screenshot.save(screenshot_path)
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Screenshot Saved'
    print(status)
    ref.update({
        'status' : status
    })
    file = File(screenshot_path, name='screenshot.png') 
    hook.send('@everyone Look at this:', file=file)
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Screenshot Sent'
    print(status)
    ref.update({
        'status' : status
    })
    pyautogui.click(found_ready)
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Ready Up Button Pressed'
    print(status)
    ref.update({
        'status' : status
    })

        
