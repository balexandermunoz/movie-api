# FastAPI
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

# App:
from utils.jwt_manager import create_token
from schemas.user import User

auth_route = APIRouter()

@auth_route.post('/', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = create_token(user.dict())
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")