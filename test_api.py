import requests

# The address of your Django server
url = "http://127.0.0.1:8000/api/diagnose/"

# Change this to the path of a real tomato image on your computer
image_path = r"C:\project\merg\Screenshot 2026-02-09 113214.png"

with open(image_path, 'rb') as f:
    # 'image' matches the name we used in views.py
    files = {'image': f}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.json())