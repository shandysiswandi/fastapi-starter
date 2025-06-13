from pydantic import BaseModel


class LoginRequest(BaseModel):
    """Request body for user login."""

    username: str
    password: str


class LoginResponse(BaseModel):
    """Response body for user login."""

    access_token: str
    refresh_token: str
    access_expiry: int
    refresh_expiry: int


class RegisterRequest(BaseModel):
    """Request body for user registration."""

    email: str
    username: str
    password: str


class RegisterResponse(BaseModel):
    """Response body for user registration."""

    access_token: str
    refresh_token: str
    access_expiry: int
    refresh_expiry: int


class ResetPasswordRequest(BaseModel):
    """Request body to initiate password reset."""

    email: str


class ResetPasswordResponse(BaseModel):
    """Response after initiating password reset."""

    email: str


class ResetPasswordConfirmRequest(BaseModel):
    """Request body to confirm a password reset."""

    token: str
    new_password: str


class ResetPasswordConfirmResponse(BaseModel):
    """Response after confirming a password reset."""

    email: str


class ChangePasswordRequest(BaseModel):
    """Request body to change an existing password."""

    old_password: str
    new_password: str


class ChangePasswordResponse(BaseModel):
    """Response after changing the password."""

    email: str


class RefreshTokenRequest(BaseModel):
    """Request body to refresh authentication tokens."""

    refresh_token: str


class RefreshTokenResponse(BaseModel):
    """Response containing new access and refresh tokens."""

    access_token: str
    refresh_token: str
    access_expiry: int
    refresh_expiry: int
