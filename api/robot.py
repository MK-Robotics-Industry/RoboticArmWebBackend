from utils.robot import send_command
from fastapi import APIRouter

from schema.robot import (
    MoveRequest,
    JointPositionRequest,
    JointSpeedRequest,
)

from websocket.manager import manager

router = APIRouter()

@router.get("/status")
def status():
    return manager.robot_status


@router.post("/home")
async def home_arm():

    await send_command({
        "type": "command",
        "command": "home",
    })

    return {
        "message": "Moving the robotic arm to the home position."
    }


@router.post("/move")
async def move_arm(request: MoveRequest):

    await send_command({
        "type": "command",
        "command": "move",
        "base": request.base,
        "shoulder": request.shoulder,
        "elbow": request.elbow,
        "wrist": request.wrist,
        "gripper": request.gripper,
        "speed": request.speed,
    })

    return {
        "message": "Move command sent successfully."
    }


@router.post("/move/base")
async def move_base(request: JointPositionRequest):

    await send_command({
        "type": "command",
        "command": "move",
        "joint": "base",
        "position": request.position,
    })

    return {
        "message": f"Base moved to {request.position}."
    }


@router.post("/move/shoulder")
async def move_shoulder(request: JointPositionRequest):

    await send_command({
        "type": "command",
        "command": "move",
        "joint": "shoulder",
        "position": request.position,
    })

    return {
        "message": f"Shoulder moved to {request.position}."
    }


@router.post("/move/elbow")
async def move_elbow(request: JointPositionRequest):

    await send_command({
        "type": "command",
        "command": "move",
        "joint": "elbow",
        "position": request.position,
    })

    return {
        "message": f"Elbow moved to {request.position}."
    }


@router.post("/move/wrist")
async def move_wrist(request: JointPositionRequest):

    await send_command({
        "type": "command",
        "command": "move",
        "joint": "wrist",
        "position": request.position,
    })

    return {
        "message": f"Wrist moved to {request.position}."
    }


@router.post("/move/gripper")
async def move_gripper(request: JointPositionRequest):

    await send_command({
        "type": "command",
        "command": "move",
        "joint": "gripper",
        "position": request.position,
    })

    return {
        "message": f"Gripper moved to {request.position}."
    }


@router.post("/move/gripper/open")
async def open_gripper():

    await send_command({
        "type": "command",
        "command": "move",
        "joint": "gripper",
        "position": 180,
    })

    return {
        "message": "Gripper opened."
    }


@router.post("/move/gripper/close")
async def close_gripper():

    await send_command({
        "type": "command",
        "command": "move",
        "joint": "gripper",
        "position": 0,
    })

    return {
        "message": "Gripper closed."
    }


@router.post("/robot/set-speed")
async def set_speed(request: JointSpeedRequest):

    await send_command({
        "type": "command",
        "command": "set-speed",
        "speed": request.speed,
    })

    return {
        "message": f"Speed set to {request.speed}."
    }


@router.post("/disable")
async def disable_arm():

    await send_command({
        "type": "command",
        "command": "disable",
    })

    return {
        "message": "Robot disabled."
    }


@router.post('/enable')
async def enable_arm():

    await send_command({
        "type": "command",
        "command": "enable",
    })

    return {
        "message": "Robot enabled."
    }