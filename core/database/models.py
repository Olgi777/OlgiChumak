from sqlalchemy import (
    Column,
    SMALLINT,
    VARCHAR,
    CheckConstraint,
    INT,
    DECIMAL,
    ForeignKey,
    TIMESTAMP,
    BOOLEAN
)
from sqlalchemy.orm import relationship
from .base import Base

__all__ = [
    "Base",
    "Account",
    "Gender",
]


class Gender(Base):
    __tablename__ = "genders"
    __table_args__ = (
        CheckConstraint("length(name) >= 2"),
        CheckConstraint("length(slug) >= 2"),
        CheckConstraint("slug not like '%%' "),
    )
    id = Column(SMALLINT, primary_key=True)
    name = Column(VARCHAR(32), nullable=False, unique=True)
    slug = Column(VARCHAR(32), nullable=False, unique=True)
    accounts = relationship(argument="Account", back_populates="gender")

    def __str__(self):
        return self.name


class Account(Base):
    __tablename__ = "accounts"
    __table_args__ = (
        CheckConstraint("length(title) >=2"),
        CheckConstraint("length(body) >=50"),
        CheckConstraint("age > 18"),
    )
    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(128), nullable=False)
    body = Column(VARCHAR(250), nullable=False)
    age = Column(DECIMAL(precision=3, scale=0), nullable=False)

    gender_id = Column(
        SMALLINT,
        ForeignKey(column="genders.id", ondelete="RESTRICT", onupdate="CASCADE"),
        nullable=False
    )

    date_created = Column(TIMESTAMP, nullable=False)
    is_published = Column(BOOLEAN, default=False)
    slug = Column(VARCHAR(128), nullable=True, unique=True)
    gender = relationship(argument="Gender", back_populates="accounts")

    def __str__(self):
        return self.title
