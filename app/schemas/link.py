from pydantic import BaseModel


class GetUrlSchema(BaseModel):
    url: str


class UrlResponse(BaseModel):
    url: str


class DbUrlRequestSchema(BaseModel):
    original_url: str
    short_code: str


class DbUrlResponseSchema(BaseModel):
    short_code: str
