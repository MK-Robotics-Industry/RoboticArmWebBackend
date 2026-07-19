from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.browsers: set[WebSocket] = set()
        self.robot: WebSocket | None = None

        self.status = {
            "connected": False,
            "moving": False,
            "enabled": False,
            "position": {
                "base": 0,
                "shoulder": 0,
                "elbow": 0,
                "wrist": 0,
                "gripper": 0
            }
        }

    @property
    def browser(self) -> WebSocket | None:
        if self.browsers:
            return next(iter(self.browsers))
        return None

    @browser.setter
    def browser(self, websocket: WebSocket | None):
        if websocket is None:
            self.browsers.clear()
        else:
            self.browsers.add(websocket)

    def connect_browser(self, websocket: WebSocket):
        self.browsers.add(websocket)

    def disconnect_browser(self, websocket: WebSocket):
        self.browsers.discard(websocket)

    async def broadcast_browser(self, data: dict):
        disconnected = []
        for ws in list(self.browsers):
            try:
                await ws.send_json(data)
            except Exception:
                disconnected.append(ws)
        for ws in disconnected:
            self.browsers.discard(ws)


manager = ConnectionManager()