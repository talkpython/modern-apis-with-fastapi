from typing import Optional

import fastapi

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def weather(city: str,
            state: Optional[str] = None,
            country: str = 'US',
            units: Optional[str] = 'metric'):

    return f"{city}, {state}, {country} in {units}"
