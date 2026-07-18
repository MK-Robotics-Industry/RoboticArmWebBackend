from schema.robot import MoveRequest
from websocket.manager import manager
from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()

@router.get("/status")
def status():
    return manager.robot_status

@router.post("/home")
def home_arm():
    return {"message": "Moving the robotic arm to the home position."}

@router.post("/move")
async def move_arm(request: MoveRequest):

    if manager.robot is None:
        raise HTTPException(
            status_code=400,
            detail="Robot not connected"
        )

    await manager.robot.send_json({
        "type": "command",
        "command": "move",
        "base": 30,
        "shoulder": 45,
        "elbow": 60,
        "wrist": 10,
        "gripper": 90,
        "speed": request.speed
    })

    return {
        "message": "Move command sent successfully."
    }