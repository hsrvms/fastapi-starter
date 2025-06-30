from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from ..database.core import DbSession
from ..rate_limiting import limiter
from . import model, service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/hour")
async def register_user(
    request: Request, db: DbSession, register_user_request: model.RegisterUserRequest
):
    service.register_user(db, register_user_request)


@router.post("/token", response_model=model.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: DbSession
):
    return service.login_for_access_token(form_data, db)
