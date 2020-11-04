from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = 'US'
