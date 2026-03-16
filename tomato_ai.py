from ultralytics import YOLO
import cv2
import tkinter as tk
from tkinter import filedialog

# 1. Setup the File Upload Window
# This keeps the "blank" tkinter window from appearing in the background
root = tk.Tk()
root.withdraw()

# 2. Ask the user to select an image file
print("📂 Opening file selector... Please pick an image.")
img_path = filedialog.askopenfilename(
    title="Select a Tomato Leaf Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
)

# Check if the user actually picked a file
if not img_path:
    print("❌ No file selected. Exiting script.")
else:
    # 3. Load your models
    detector = YOLO("C:/Users/Hp/Downloads/tomato_best_float16.tflite", task="detect")
    classifier = YOLO("C:/Users/Hp/Downloads/tomato_disease_v2_50e.pt", task="classify")

    # 4. Process the uploaded image
    img = cv2.imread(img_path)
    results = detector(img)

    final_label = "None"
    max_conf = 0.0

    # Scan every leaf detected
    for r in results:
        for box in r.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            leaf_crop = img[y1:y2, x1:x2]
            
            # Use 320px high-resolution for better accuracy on Bacterial Spot
            disease_results = classifier(leaf_crop, imgsz=320)
            label = disease_results[0].names[disease_results[0].probs.top1]
            conf = disease_results[0].probs.top1conf.item()

            # Keep only the result with the highest confidence
            if conf > max_conf:
                max_conf = conf
                final_label = label

    # 5. Print the SINGLE final answer
    if max_conf > 0:
        print(f"\n--- Analysis Complete ---")
        print(f"📸 Image: {img_path.split('/')[-1]}")
        print(f"🎯 Final Diagnosis: {final_label} ({max_conf*100:.1f}%)")
    else:
        print("❌ No tomato leaves were detected in the selected image.")