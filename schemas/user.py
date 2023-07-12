from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: str = EmailStr()
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "admin@gmail.com",
                "password": "admin",
            }
        }
