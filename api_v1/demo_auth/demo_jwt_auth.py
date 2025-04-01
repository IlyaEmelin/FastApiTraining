from jwt.exceptions import InvalidTokenError
from typing import Any

from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
    OAuth2PasswordBearer,
)
from pydantic import BaseModel
from users.schemas import UserSchema
from auth.utils import hash_password, encode_jwt, validate_password, decode_jwt

# http_bearer = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/demo-auth/jwt/login/",
)


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


router = APIRouter(prefix="/jwt", tags=["JWT"])

join = UserSchema(
    username="Join",
    password=hash_password("qwerty"),
    email="join@example.com",
)
ivan = UserSchema(
    username="Ivan",
    password=hash_password("123456"),
)

user_db: dict[str, UserSchema] = {
    join.username: join,
    ivan.username: ivan,
}


def validate_auth_user_login(
    username: str = Form(),
    password: str = Form(),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )
    if not (user := user_db.get(username)):
        raise unauthed_exc
    if not validate_password(password=password, hashed_password=user.password):
        raise unauthed_exc
    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user inactive",
        )
    return user


def get_current_token_payload(
    # credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
    token: str = Depends(oauth2_scheme),
) -> dict[str, Any]:
    # token = credentials.credentials
    try:
        payload = decode_jwt(token=token)
    except InvalidTokenError as exp:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            # detail=f"invalid token error: {exp}",
            detail=f"invalid token error",
        )

    return payload


def get_current_auth_user(
    payload: dict[str, Any] = Depends(get_current_token_payload),
) -> UserSchema:
    username: str | None = payload.get("sub")
    if user := user_db.get(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_current_active_auth_user(
    user: UserSchema = Depends(get_current_auth_user),
):
    if not user.active:
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user inactive",
        )
    return user


@router.post("/login/", response_model=TokenInfo)
def auth_user_issue_jwt(
    user: UserSchema = Depends(validate_auth_user_login),
):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    token = encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )


@router.get("/users/me/")
def auth_user_check_self_info(
    payload: dict[str, Any] = Depends(get_current_token_payload),
    user: UserSchema = Depends(get_current_active_auth_user),
):
    iad = payload.get("iad")
    return {
        "username": user.username,
        "email": user.email,
        "logged_in_at": iad,
    }
