from faseapi import APIRouter
from app.services.camera import get_frame
from app.core.detector import detect

router = APIRouter()

@router.get("/detect")
def detect_api():
  frame = get_frame()
  if frame is None:
    return{"error" : "Camera Not Working"}
  detections = detect(frame)
  return{"detections" : detections}
    
