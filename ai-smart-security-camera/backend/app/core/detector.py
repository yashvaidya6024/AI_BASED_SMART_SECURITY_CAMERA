from app.core.model import get_model

def detect(frame):
  model = get_model()
  result = model(frame)
  detections = []

for box in results[0].boxes.data.tolist():
  detections.append({
    "x1" : box[0],
    "y1" : box[1],
    "x2" : box[2],
    "y2" : box[3],
    "confidence" : box[4]
    "class" : int(box[5])
  })
  return detections
