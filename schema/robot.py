from pydantic import BaseModel


class MoveRequest(BaseModel):
    base: float | None = None
    shoulder: float | None = None
    elbow: float | None = None
    wrist: float | None = None
    gripper: float | None = None
    speed: int = 100


class JointPositionRequest(BaseModel):
    position: int


class JointSpeedRequest(BaseModel):
    speed: int