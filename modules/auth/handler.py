from typing import Annotated

from fastapi import APIRouter, Depends, Request

from modules.auth.schema import (
    ChangePasswordRequest,
    ChangePasswordResponse,
    LoginRequest,
    LoginResponse,
    RefreshTokenRequest,
    RefreshTokenResponse,
    RegisterRequest,
    RegisterResponse,
    ResetPasswordConfirmRequest,
    ResetPasswordConfirmResponse,
    ResetPasswordRequest,
    ResetPasswordResponse,
)
from modules.auth.service import AuthService
from modules.response import APIResponse

AuthRouter = APIRouter(tags=["Auth"])


@AuthRouter.post(
    path="/auth/login",
    response_model=APIResponse[LoginResponse],
    summary="User Login",
    description="Authenticate a user and return access and refresh tokens.",
)
async def login(
    body: LoginRequest,
    req: Request,
    srv: Annotated[AuthService, Depends()],
):
    """Authenticate a user and return access and refresh tokens."""
    response = LoginResponse(
        access_token="",
        refresh_token="",
        access_expiry=1,
        refresh_expiry=1,
    )
    return APIResponse(message="login", data=response)


@AuthRouter.post(
    path="/auth/register",
    response_model=APIResponse[RegisterResponse],
    summary="User Registration",
    description="Create a new user account with username, password, and other details.",
)
async def register(
    body: RegisterRequest,
    req: Request,
    srv: Annotated[AuthService, Depends()],
):
    """Register a new user account."""
    return {"message": "register"}


@AuthRouter.post(
    path="/auth/reset-password",
    response_model=APIResponse[ResetPasswordResponse],
    summary="Initiate Password Reset",
    description=(
        "Send a password reset request (e.g., via email) to "
        "start the password reset process."
    ),
)
async def reset_password(
    body: ResetPasswordRequest,
    req: Request,
    srv: Annotated[AuthService, Depends()],
):
    """Initiate the password reset process by email."""
    return {"message": "reset_password"}


@AuthRouter.post(
    path="/auth/reset-password/confirm",
    response_model=APIResponse[ResetPasswordConfirmResponse],
    summary="Confirm Password Reset",
    description=(
        "Confirm and complete the password reset using a "
        "valid reset token and new password."
    ),
)
async def reset_password_confirm(
    body: ResetPasswordConfirmRequest,
    req: Request,
    srv: Annotated[AuthService, Depends()],
):
    """Confirm a password reset using a token and new password."""
    return {"message": "reset_password_confirm"}


@AuthRouter.post(
    path="/auth/refresh",
    response_model=APIResponse[RefreshTokenResponse],
    summary="Refresh Access Token",
    description="Use a valid refresh token to obtain a new access token.",
)
async def refresh_token(
    body: RefreshTokenRequest,
    req: Request,
    srv: Annotated[AuthService, Depends()],
):
    """Refresh the access token using a valid refresh token."""
    return {"message": "refresh_token"}


# need token


@AuthRouter.get(
    path="/auth/change-password",
    response_model=APIResponse[RegisterResponse],
    summary="Change Password",
    description="Change the current user's password. Authentication is required.",
)
async def current_user(
    req: Request,
    srv: Annotated[AuthService, Depends()],
):
    """Return the currently authenticated user's information."""
    return {"message": "current_user"}


@AuthRouter.post(
    path="/auth/me",
    response_model=APIResponse[ChangePasswordResponse],
    summary="Get Current User",
    description="Return details of the authenticated user.",
)
async def change_password(
    body: ChangePasswordRequest,
    req: Request,
    srv: Annotated[AuthService, Depends()],
):
    """Change the authenticated user's password."""
    return {"message": "change_password"}
