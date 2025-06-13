from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    access_expiry: int
    refresh_expiry: int


class RegisterRequest(BaseModel):
    email: str
    username: str
    password: str


class RegisterResponse(BaseModel):
    access_token: str
    refresh_token: str
    access_expiry: int
    refresh_expiry: int


class ResetPasswordRequest(BaseModel):
    email: str


class ResetPasswordResponse(BaseModel):
    email: str


class ResetPasswordConfirmRequest(BaseModel):
    token: str
    new_password: str


class ResetPasswordConfirmResponse(BaseModel):
    email: str


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str


class ChangePasswordResponse(BaseModel):
    email: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    access_expiry: int
    refresh_expiry: int
