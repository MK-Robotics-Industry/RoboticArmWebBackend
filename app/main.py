from fastapi import FastAPI
from api import robot
app = FastAPI(
    title="Robotic Arm Backend",
    version="1.0.0"
)

app.include_router(
    robot.router,
    prefix="/robot",
    tags=["Robot"]
)


@app.get("/")
def status():
    return {"message": "robotic arm backend is running"}
