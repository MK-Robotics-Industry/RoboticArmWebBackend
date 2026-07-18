from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.browser: WebSocket | None = None
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


manager = ConnectionManager()