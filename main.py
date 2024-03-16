import time
import pyautogui
import time
import pydirectinput
from dhooks import Webhook , File
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import subprocess
import platform
import re
with open('settings.txt', 'r') as file:
    # Read the file line by line
    lines = file.readlines()
    # Iterate over the lines
    for line in lines:
        startFN_match = re.search(r'FNSTART="([^"]+)"', line)
        if startFN_match:
            startFN_value = startFN_match.group(1)
variable_to_send = "True"
with open("var.txt", "w") as file:
    file.write(variable_to_send)
def start_other_script(script_name):
    try:
        if platform.system() == "Windows":
            # Use subprocess.STARTUPINFO to hide the window
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen(["pythonw", script_name], startupinfo=startupinfo)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "Terminal", "pythonw", script_name])
        elif platform.system() == "Linux":
            subprocess.Popen(["x-terminal-emulator", "-e", "pythonw", script_name])
        else:
            print("Unsupported platform:", platform.system())
    except Exception as e:
        print(f"Error starting {script_name}:", e)

if __name__ == "__main__":
    scripts_to_run = ["wifioff_1.0.pyw", "glider_2.0.pyw","screenshotbutton_2.2.pyw","off_1.0.pyw"]
    for script in scripts_to_run:
        start_other_script(script)
cred = credentials.Certificate("Tools/creds.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': str('')
})
ref = db.reference('/WSTFN')
desktop_dir = os.path.join(os.environ['USERPROFILE'], 'Desktop')
if startFN_value == "True":
    # Example: Run multiple commands without opening a new cmd window
    commands = 'cd /d {} && Fortnite.url'.format(desktop_dir)
    subprocess.run(commands, shell=True)
    def is_start_present(text):
        return "PLAY" in text.lower()
    while True:
        screenshot = pyautogui.screenshot()
        grayscale_image = screenshot.convert('L')
        width, height = grayscale_image.size
        search_region = (0, 0, width, height)
        found_start = pyautogui.locateOnScreen('Images/play.png', grayscale=True, region=search_region, confidence=0.8)
        if found_start:
            pyautogui.click(found_start)
            time.sleep(2)
            def is_start_present2(text):
                return "PLAY" in text.lower()
            screenshot = pyautogui.screenshot()
            grayscale_image = screenshot.convert('L')
            width, height = grayscale_image.size
            search_region = (0, 0, width, height)
            found_start2 = pyautogui.locateOnScreen('Images/play.png', grayscale=True, region=search_region, confidence=0.8)
            if found_start2:
                pyautogui.click(found_start2)
            break
        else: 
            pyautogui.scroll(100)
            pyautogui.press('esc')
            time.sleep(1)
while True:
    hook = Webhook('')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Waiting for match to start'
    print(status)
    ref.update({
        'status' : status
    })
    def is_doors_present(text):
        return "BATTLE" in text.lower()
    while True:
        screenshot = pyautogui.screenshot()
        grayscale_image = screenshot.convert('L')
        width, height = grayscale_image.size
        search_region = (0, 0, width, height)
        found_doors = pyautogui.locateOnScreen('Images/Battle.png', grayscale=True, region=search_region)
        if found_doors:
            status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Match Started'
            print(status)
            ref.update({
                'status' : status
            })
            break
        time.sleep(1)
    pyautogui.press('a')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Closed Augments'
    print(status)
    ref.update({
        'status' : status
    })
    pyautogui.press('m')
    time.sleep(0.5)
    pyautogui.click(2083,1275) # tree (2012,1210) #bush (2024,1222)
    time.sleep(0.1)
    pyautogui.press('m')
    pyautogui.click()
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Pinged Drop'
    print(status)
    ref.update({
        'status' : status
    })
    time.sleep(26)
    pyautogui.press('b')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.keyDown('space')
    time.sleep(0.2)
    pyautogui.keyUp('space')
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Deployed Glider'
    print(status)
    ref.update({
        'status' : status
    })
    i =10
    while i > 0:
        pydirectinput.moveRel(0, 1000, relative=True)
        i-=1
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Positioned Camera At Floor'
    print(status)
    ref.update({
        'status' : status
    })
    status = '['+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+'] '+'Gliding To Marker'
    print(status)
    ref.update({
        'status' : status
    })
    variable_to_send = "False"
    with open("var.txt", "w") as file:
        file.write(variable_to_send)
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
            variable_to_send = "True"
            with open("var.txt", "w") as file:
                file.write(variable_to_send)
            break
        else:
            def is_doors_present(text):
                return "READY" in text.lower()
            screenshot = pyautogui.screenshot()
            grayscale_image = screenshot.convert('L')
            width, height = grayscale_image.size
            search_region = (0, 0, width, height)
            found_ready = pyautogui.locateOnScreen('Images/ready3.png', grayscale=True, region=search_region, confidence=0.75)
            if found_ready:
                break 
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
        found_ready = pyautogui.locateOnScreen('Images/ready3.png', grayscale=True, region=search_region, confidence=0.75)
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
    hook.send('@everyone New Placement:', file=file)
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

        
