import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin SDK
cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred)

# Get storage bucket URL
storage_bucket_url = firebase_admin.get_app().options['storageBucket']
print("Storage Bucket URL:", storage_bucket_url)
