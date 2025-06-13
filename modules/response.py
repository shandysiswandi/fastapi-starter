from enum import StrEnum
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ErrorType(StrEnum):
    """Enumeration of error types for API responses."""

    validation = "Validation Error"
    business = "Business"
    internal = "Internal System"


class APIResponse(BaseModel, Generic[T]):
    """Generic API response wrapper for success cases.

    Includes a message and either a single item or list of items.
    """

    message: str
    data: T | list[T]


class APIError(BaseModel):
    """Standardized structure for API error responses."""

    message: str
    type: ErrorType
    detail: list[dict] | None = None
