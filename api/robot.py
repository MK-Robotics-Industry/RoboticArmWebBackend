from websocket.manager import manager
from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return manager.robot_status

@router.post("/home")
def home_arm():
    return {"message": "Moving the robotic arm to the home position."}

@router.post("/move")
def move_arm():
    return {"message": "Moving the robotic arm to the specified position."}