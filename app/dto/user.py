from datetime import datetime
from typing import Optional
from dataclasses import dataclass

from litestar.dto import DataclassDTO, DTOConfig
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    surname: str
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    password: Optional[str] = None


@dataclass
class UserOut:
    id: int
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime


class UserDTO(DataclassDTO[UserOut]):
    config = DTOConfig(exclude={"password"})