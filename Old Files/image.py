import os
import time
import pyautogui
import firebase_admin
from firebase_admin import credentials, storage, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'logtestwst.appspot.com',
    'databaseURL': 'https://logtestwst-default-rtdb.firebaseio.com/'
})

# Upload screenshot to Firebase Storage and Realtime Database
def upload_screenshot():
    # Capture screenshot
    screenshot = pyautogui.screenshot()
    
    # Save screenshot locally with a unique filename based on timestamp
    timestamp = int(time.time())
    screenshot_path = f"screenshot_{timestamp}.png"
    screenshot.save(screenshot_path)
    
    # Upload screenshot to Firebase Storage
    bucket = storage.bucket()
    destination_path = f"screenshot_{timestamp}.png"  # Adjust the destination path as needed
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(screenshot_path)
    blob.make_public()
    image_url = blob.public_url
    
    # Add screenshot URL and timestamp to Realtime Database
    ref = db.reference('WSTFN')
    ref.update({'Current_SS': image_url})
    
    return image_url, screenshot_path

# Delete old screenshot from Firebase Storage
# Delete old screenshot from Firebase Storage
def delete_old_screenshot(old_screenshot_path):
    if old_screenshot_path:
        bucket = storage.bucket()
        blob = bucket.blob(old_screenshot_path)
        if blob.exists():
            blob.delete()
            print("Old screenshot deleted from Firebase Storage.")
        else:
            print("Old screenshot does not exist in Firebase Storage.")

# Main function
def main():
    old_screenshot_path = None
    while True:
        # Upload screenshot every 5 seconds
        image_url, screenshot_path = upload_screenshot()
        print("Screenshot uploaded:", image_url)
        
        # Delete the old screenshot from Firebase Storage
        delete_old_screenshot(old_screenshot_path)
        old_screenshot_path = screenshot_path
        
        # Delete the old screenshot from local filesystem
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
            print("Old screenshot deleted.")
        else:
            print("The file does not exist.")
        
        time.sleep(45)

if __name__ == "__main__":
    main()
