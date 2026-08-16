from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from app.database import Base


# Модель таблицы links
class Link(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(String)
    short_code: Mapped[str] = mapped_column(String, unique=True)
