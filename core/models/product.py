from core.models.base import Base, Mapped


class Product(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
