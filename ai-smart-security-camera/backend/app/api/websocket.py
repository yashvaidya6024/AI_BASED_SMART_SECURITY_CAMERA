from fastapi import APIRouter, WebSocket
import cv2
from app.core.detector import detect

websocket_router = APIRouter()

@websocket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        detections = detect(frame)
        await websocket.send_json({"detections": detections})
