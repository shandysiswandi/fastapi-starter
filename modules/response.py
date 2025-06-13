from typing import List, Optional, Union, Generic, TypeVar
from enum import Enum
from pydantic import BaseModel

T = TypeVar("T")


class ErrorType(str, Enum):
    validation = "Validation Error"
    business = "Business"
    internal = "Internal System"


class APIResponse(BaseModel, Generic[T]):
    message: str
    data: Union[T, List[T]]


class APIError(BaseModel):
    message: str
    type: ErrorType
    detail: Optional[List[dict]] = None
