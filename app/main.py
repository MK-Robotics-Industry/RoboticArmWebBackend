from fastapi import FastAPI
from api import robot
from websocket.browser import router as browser_router
from websocket.robot import router as robot_router

app = FastAPI(
    title="Robotic Arm Backend",
    version="1.0.0"
)

app.include_router(
    robot.router,
    prefix="/robot",
    tags=["Robot"]
)

app.include_router(browser_router)
app.include_router(robot_router)

@app.get("/")
def status():
    return {"message": "robotic arm backend is running"}
