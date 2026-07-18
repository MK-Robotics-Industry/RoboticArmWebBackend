from fastapi import HTTPException
from websocket.manager import manager


def ensure_robot_connected() -> None:
    if manager.robot is None:
        raise HTTPException(
            status_code=400,
            detail="Robot not connected"
        )


async def send_command(command: dict) -> None:
    ensure_robot_connected()
    await manager.robot.send_json(command)