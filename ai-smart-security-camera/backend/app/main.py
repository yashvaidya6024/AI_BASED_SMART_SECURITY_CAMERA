from fastapi import FastAPI
from app.api.routes import router
from app.api.websocket import websocket_router

app = FastAPI()

app.include_router(router)
app.include_router(websocket_router)

@app.get("/")
def home():
    return {"message": "AI Security Camera Running"}
