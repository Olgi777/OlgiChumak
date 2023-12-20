from typing import Annotated, Any
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from .alchemy import SQLAlchemyRepository
from .abstract import AbstractRepository
from ..database import Gender as GenderModel
from ..types import GenderDetail

__all__ = [
    "Gender",
    "gender_manager"
]


class GenderRepository(SQLAlchemyRepository):
    model = GenderModel
    # model = "genders"
    schema = GenderDetail
    # pk = "id"


class GenderManager(AbstractRepository):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def get(self, pk: Any) -> BaseModel:
        obj = self.repository.get(pk=pk)
        if obj is not None:
            return obj
        raise HTTPException(status_code=404, detail="gender not found")

    def create(self, obj: BaseModel) -> BaseModel:
        try:
            obj = self.repository.create(obj=obj)
        except:
            raise HTTPException(status_code=status.HTTP_404_BAD_REQUEST, detail="gender exist")
        else:
            return obj

    def update(self, pk: Any, obj: BaseModel) -> BaseModel:
        try:
            obj = self.repository.update(pk=pk, obj=obj)
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid")
        else:
            return obj

    def delete(self, pk: Any) -> None:
        self.repository.delete(pk=pk)

    def all(self) -> list[BaseModel]:
        return self.repository.all()


gender_repository = GenderRepository()
gender_manager = GenderManager(repository=gender_repository)

Gender = Annotated[GenderModel, Depends(dependency=lambda: gender_manager)]
