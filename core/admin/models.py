from sqladmin import ModelView
from ..database import Account, Gender
from ..forms import AccountForm, GenderForm

__all__ = [
    "AccountAdmin",
    "GenderAdmin"
]


class AccountAdmin(ModelView, model=Account):
    name_plural = "аккаунт"
    column_list = ["title", "is_publiched", "date_created"]

    # form = AccountForm


class GenderAdmin(ModelView, model=Gender):
    name_plural = "пол"
    column_list = ["name"]
    # form = GenderForm
