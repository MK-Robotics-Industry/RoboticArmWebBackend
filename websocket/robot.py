from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websocket.manager import manager

router = APIRouter()


@router.websocket("/ws/robot")
async def robot_socket(websocket: WebSocket):

    await websocket.accept()

    manager.robot = websocket

    print("Robot Connected")

    try:

        while True:

            message = await websocket.receive_text()

            print("Robot:", message)

            if manager.browser:

                await manager.browser.send_text(message)

    except WebSocketDisconnect:

        print("Robot Disconnected")

        manager.robot = None