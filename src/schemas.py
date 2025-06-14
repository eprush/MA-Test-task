from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


class CookiesSchema(BaseModel):
    sc: str = Field(
        ...,
        description="Cookie value",
        max_length=100,
        min_length=50,
        frozen=True,
    )
    sentrysid: str = Field(
        ...,
        max_length=100,
        min_length=50,
        frozen = True,
    )

class EntryResponseSchema(BaseModel):
    content_type: Literal["text/html"]
    connection: Literal["keep-alive"]
    vary: Literal["Accept-Language, Cookie"]
    cookies: CookiesSchema

    model_config = ConfigDict(from_attributes=True)

