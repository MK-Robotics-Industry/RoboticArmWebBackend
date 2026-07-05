from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        self.browser: WebSocket | None = None
        self.robot: WebSocket | None = None


manager = ConnectionManager()