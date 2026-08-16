from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

async_engine = create_async_engine(
    url="postgresql+asyncpg://postgres:password@localhost:5432/myapp"
)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
