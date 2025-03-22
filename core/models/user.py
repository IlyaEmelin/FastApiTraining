from sqlalchemy import String
from core.models.base import Base, Mapped, mapped_column


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
