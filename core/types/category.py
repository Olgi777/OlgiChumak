from pydantic import PositiveInt, Field
from .base import Schema
from .custom import SlugStr

__all__ = [
    "GenderDetail"
]


class GenderDetail(Schema):
    id: PositiveInt = Field(
        default=...,
        title="Gender ID",
        examples=[42]
    )
    name: str = Field(
        default=...,
        title="Gender Name",
        min_length=2,
        max_length=32,
        examples=["Girl"]
    )
    slug: SlugStr = Field(
        default=...,
        title="Gender URL",
        min_length=2,
        max_length=32,
        examples=["man"]
    )
