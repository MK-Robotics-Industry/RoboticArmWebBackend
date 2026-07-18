import json
from dataclasses import dataclass
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websocket.manager import manager

router = APIRouter()


@router.websocket("/ws/robot")
async def robot_socket(websocket: WebSocket):

    await websocket.accept()

    manager.robot = websocket
    manager.status["connected"] = False

    try:

        while True:

            message = await websocket.receive_text()
            data = json.loads(message)

            if data.get('type') == "status":
                manager.status.update(data)

            if manager.browser:
                await manager.browser.send_json(manager.status)

    except WebSocketDisconnect:
        
        manager.robot = None
        manager.status["connected"] = False


