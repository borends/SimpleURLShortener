import secrets

from sqlalchemy import select

from app.database import async_session_factory
from app.models.link import Link


async def make_short_link(url: str):
    async with async_session_factory() as session:
        new_link = Link(
            original_url=url,
            short_code=secrets.token_urlsafe(5)[:5]
        )
        session.add(new_link)
        await session.commit()

        await session.refresh(new_link)  # Обновляет объект новыми данными из БД
        return {"short_link": new_link.short_code}


async def find_link(code: str) -> str:
    async with async_session_factory() as session:
        query = select(Link).filter_by(short_code=code)
        result = await session.execute(query)
        return result.scalar_one_or_none().original_url
