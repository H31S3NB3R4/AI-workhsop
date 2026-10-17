"""YOLO Image Object Detection"""

import cv2
from ultralytics import YOLO

# 1. Load your trained model
model = YOLO("best_4.pt")

# 2. Set the path to your image
image_path = "20170815-rock-scissors-pixabay-34f3h8kx0ucail5dbcp8n4.jpg"

# 3. Read the image from disk
frame = cv2.imread(image_path)

if frame is None:
    raise FileNotFoundError(f"Could not read the image: {image_path}")

# 4. Detect objects in the image
results = model(frame, conf=0.2)  # conf=0.5, verbose=False

# 5. Draw bounding boxes, class names, and confidence scores
annotated_frame = results[0].plot()

# 6. Display the annotated image (press any key to close)
cv2.imshow("YOLO Image Detection", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Optionally save the result
cv2.imwrite("output.jpg", annotated_frame)
print("Saved annotated image to output.jpg")