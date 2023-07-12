# FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# App:
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routes.movie import movie_router
from routes.auth import auth_route

app = FastAPI()
app.title = "FakeAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router, prefix="/movie")
app.include_router(auth_route, prefix="/login")

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello world!</h1>')
