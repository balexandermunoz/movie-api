import os
from dotenv import load_dotenv
from jwt import encode, decode

load_dotenv()


def create_token(data: dict) -> str:
    token: str = encode(payload=data, key=os.environ["TOKEN_KEY"], algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data = decode(token, key=os.environ["TOKEN_KEY"], algorithms=["HS256"])
    return data