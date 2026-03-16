from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from ultralytics import YOLO
import cv2
import numpy as np

# Load your models
# IMPORTANT: Double check these file paths match where your models are!
detector = YOLO("C:/Users/Hp/Downloads/tomato_best_float16.tflite", task="detect")
classifier = YOLO("C:/Users/Hp/Downloads/tomato_disease_v2_50e.pt", task="classify")

class PredictDisease(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # 1. Get the image from the request
        if 'image' not in request.FILES:
            return Response({"error": "No image provided"}, status=400)
            
        file = request.FILES['image']
        img_array = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # 2. Run Detection
        results = detector(img)
        max_conf = 0.0
        final_label = "No leaf detected"

        # 3. Logic to find the leaf with highest confidence
        for r in results:
            for box in r.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box)
                leaf_crop = img[y1:y2, x1:x2]
                
                # Run Classification on the cropped leaf
                disease_results = classifier(leaf_crop, imgsz=320)
                label = disease_results[0].names[disease_results[0].probs.top1]
                conf = disease_results[0].probs.top1conf.item()

                if conf > max_conf:
                    max_conf = conf
                    final_label = label

        # 4. Return the JSON result
        return Response({
            "label": final_label,
            "confidence": round(max_conf * 100, 2)
        })