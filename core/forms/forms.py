from datetime import datetime
from sqladmin.fields import DateTimeField
from sqlalchemy import select
from wtforms import Form, TextAreaField, StringField, DecimalField, BooleanField
from wtforms.validators import length, number_range
from slugify import slugify
from core.database import Gender, session

__all__ = [
    "AccountForm",
    "GenderForm"
]


class GenderForm(Form):
    name = StringField(
        label="Пол"
    )
    slug = StringField(
        label="URL",
        default=None
    )

    def validate_slug(self, field):
        self.slug.data = slugify(self.name.data)


def load_genders() -> list[tuple]:
    with session() as s:
        obj = s.scalars(
            select(Gender)
            .order_by(Gender.id)
        )
        return [(gen.id, gen.name) for gen in obj.all()]


class AccountForm(Form):
    title = StringField(
        label="Имя",
        validators=[
            length(min=2, max=200, message="Имя пользователя должно быть от 2 до 200 символов")
        ]
    )
    body = TextAreaField(
        label="О себе",
        validators=[
            length(min=100, max=2000)
        ]
    )
    age = DecimalField(
        label="Возраст",
        validators=[
            number_range(
                min=18,
                max=100
            )
        ]
    )
    date_created = DateTimeField(
        label="Дата создания",
        default=datetime.utcnow()
    )
    gender_id = StringField(
        label="Пол"
    )
    is_published = BooleanField(
        label="Опубликовано",
        default=False
    )
    slug = StringField(
        label="URL",
        default=None
    )

    def validate_slug(self, field):
        self.slug.data = slugify(f"{self.title.data}{self.date_created.data.timestamp()}")
