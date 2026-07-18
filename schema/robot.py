from pydantic import BaseModel


class MoveRequest(BaseModel):
    x: float
    y: float
    z: float
    roll: float
    pitch: float
    yaw: float
    speed: int = 100

class JointPositionRequest(BaseModel):
    position: int

class JointSpeedRequest(BaseModel):
    speed:int    