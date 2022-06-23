from typing import List
from fastapi import APIRouter, HTTPException

from app.models.user import User

router = APIRouter()


users: List[User] = []


@router.post('/', status_code=201)
def create_user(user: User):
    try:
        users.append(user)
    except Exception as error:
        raise HTTPException(status_code=500)


@router.get('/', status_code=200)
def get_all_users(name: str = None):
    try:
        return users
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500)
