from decimal import Decimal
from typing import Optional
from datetime import datetime, UTC

from pydantic import Field, PositiveInt
from .base import Schema

__all__ = [
    "AccountCreate",
    "AccountEdit",
    "AccountDetail"
]


class AccountCreate(Schema):
    title: str = Field(
        default=...,
        title="Account Title",
        min_length=2,
        max_length=128,
        examples=["I want to get to know you"]
    )
    body: str = Field(
        default=...,
        min_length=20,
        max_length=250,
        title="AccountDescription",
        examples=["Looking for a girl for a serious relationship"]
    )
    age: Decimal = Field(
        default=...,
        max_digits=3,
        decimal_places=0,
        title="The Age",
        examples=[35],
        gt=0
    )
    gender_id: PositiveInt = Field(
        default=...,
        title="Account Category ID",
        examples=[42],
    )
    date_created: datetime = Field(
        default_factory=datetime.utcnow
    )

    is_published: bool = Field(default=False)


class AccountEdit(AccountCreate):
    ...


class AccountDetail(AccountCreate):
    id: PositiveInt = Field(
        default=...,
        title="Account ID",
        examples=[42]
    )
