from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.schemas.link import GetUrlSchema
from app.services.link import make_short_link, find_link

router = APIRouter(
    tags=["link"],
)


@router.post("/short_link")
async def short_link(url: GetUrlSchema):
    return await make_short_link(url.url)


@router.get("/{code}")
async def get_link(code: str):
    url_data = await find_link(code)
    return RedirectResponse(
        url=url_data,
        status_code=307
    )
