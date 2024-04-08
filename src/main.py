from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from operations.router import router as router_operations
from tasks.router import router as task_router
from pages.router import router as pages_router
from chat.router import router as chat_router

from fastapi.staticfiles import StaticFiles
from .config import REDIS_HOST, REDIS_PORT


app = FastAPI(
    title="Trading App"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


app.mount("/static", StaticFiles(directory="static"), name="static")



app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operations)
app.include_router(task_router)
app.include_router(pages_router)
app.include_router(chat_router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")







"==============lesson 5================"
# from fastapi import FastAPI, Depends
# from fastapi_users import fastapi_users, FastAPIUsers
# from src.auth.schemas import UserRead, UserCreate
# from src.auth.manager import get_user_manager
# from src.auth.base_config import auth_backend
# from auth.database import User

# app = FastAPI(
#     title='Trading App'
# )

# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )


# current_user = fastapi_users.current_user()

# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.email}"

# @app.get("/upprotected-route")
# def protected_route():
#     return f"Hello,"




"=============  lesson 1.2.3.4================="
# from typing import List
# from pydantic import BaseModel, Field
# from datetime import datetime
# from enum import Enum
# from typing import Optional, List


# class Trade(BaseModel):
#     id: int
#     user_id: int
#     currenty: str
#     side: str
#     price: float = Field(ge=0)
#     amount: float

# class DegreeType(Enum):
#     newbue = 'Новичок'
#     expert = 'Эксперт'

# class Degree(BaseModel):
#     id: int
#     created_at: datetime
#     type_degree: DegreeType



# class User(BaseModel):
#     id: int
#     role: str
#     name: str
#     degree: Optional[List[Degree]] = []

# fake_users = [
#     {'role': 'admin', 'id': 1, 'name': 'almash'},
#     {'role': 'admikALKn', 'id': 2, 'name': 'almash'},
#     {'role': 'admiLNLn', 'id': 3, 'name': 'almash'},
# ]

# @app.get("/users/{user_id}", response_model=List[User])
# def user(user_id: int):
#     return [user for user in fake_users if user.get('id') == user_id]


# fake_trading = [
#     {'id': 1, 'user_id': 1, 'currenty': 'BTS', 'side': 'buy', 'price': 123, 'amount': 2.12},
#     {'id': 1, 'user_id': 1, 'currenty': 'BTS', 'side': 'sell', 'price': 55, 'amount': 2.12},
#     {'id': 1, 'user_id': 1, 'currenty': 'BTS', 'side': 'buy', 'price': 869, 'amount': 2.12},
# ]

# @app.get('/trades')
# def get_trades(limit: int, offset: int):
#     return fake_trading[offset:][:limit]


# fake_user2 = [
#     {'id': 1, 'role': 'admin', 'name': 'Almash'},
#     {'id': 2, 'role': 'admin', 'name': 'Almash'},
#     {'id': 3, 'role': 'admin', 'name': 'Almash'},
# ]

# @app.post("/users/{user_id}")
# def change_user_name(user_id: int, new_name):
#     current_user = list(filter(lambda user: user.get('id') == user_id, fake_user2))[0]
#     current_user['name'] = new_name
#     return {'status': 200, 'data': current_user}


# @app.post('/trades')
# def add_trades(trades: List[Trade]):
#     fake_trading.extend(trades)
#     return {'data': fake_trading}



# сперва идет название экземпляра класса FastAPI а потом через точку метод
# @app.get('/')
# def hello():
#     return 'Hello , World'
