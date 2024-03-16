import requests
import os
import time
def wifi():    
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False
    
while True:
    wifi()
    if wifi():
        print("Connected")
    else:
        os.system('shutdown -p')
    time.sleep(5)