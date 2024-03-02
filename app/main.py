"""Main module for test fastapi"""

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

from app.models.user import User, UserWithAdult
from app.models.models import SNums
from app.models.feedback import Feedback

app = FastAPI()


fake_db = {
    1: User(id=1, name="Denis Kratos", age=20),
    2: User(id=2, name="Kraded Nistos", age=21),
}


@app.get("/")
async def root():
    """Index root page"""
    return FileResponse("app/templates/index.html")


@app.get("/users")
async def get_users() -> list[User]:
    """Get users"""
    my_user1 = User(id=10, name="Denis Kratos", age=20)
    my_user2 = User(id=11, name="Kraded Nistos", age=21)
    return {"users": [my_user1, my_user2]}


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    """Get user"""
    return fake_db.get(user_id, {"message": "Такого юзера нет"})


@app.post("/check-adult", response_model=UserWithAdult)
async def check_adult(req_user: User):
    """Create user if adult"""
    res_user = UserWithAdult(**req_user.model_dump())
    return res_user


@app.post("/feedback")
async def send_feedback(feedback: Feedback):
    """Send feedback"""
    return {"message": f"Thanks, for your feedback, {feedback.model_dump().get("name", "Anonymous")}"}


@app.post("/calculate")
async def calculate(body: SNums):
    """Endpoint for sum two numbers"""
    result = body.num1 + body.num2
    return JSONResponse({"result": result})
