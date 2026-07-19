from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websocket.manager import manager

router = APIRouter()


@router.websocket("/ws/browser")
async def browser_socket(websocket: WebSocket):

    await websocket.accept()
    manager.connect_browser(websocket)

    await websocket.send_json(manager.status)

    try:
        while True:
            # Keep the connection alive
            await websocket.receive_text()

    except WebSocketDisconnect:

        print("Browser Disconnected")
        manager.disconnect_browser(websocket)