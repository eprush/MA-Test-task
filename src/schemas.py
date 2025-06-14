from pydantic import BaseModel, Field, ConfigDict

class CookieSchema(BaseModel):
    content_type: str = "text/html"
    connection: str = "keep-alive"
    vary: str = "Accept-Language, Cookie"
    cookie: str = Field(
        ...,
        max_length=100,
        min_length=50
    )

    model_config = ConfigDict(from_attributes=True)

