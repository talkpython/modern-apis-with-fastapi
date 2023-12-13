import json
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from services import openweather_service
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f'WARNING: {file} file not found, you cannot continue, please see settings_template.json')
        raise Exception('settings.json file not found, you cannot continue, please see settings_template.json')

    with open(file) as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get('api_key')


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == '__main__':
    configure()
    # uvicorn was updated, and it's type definitions don't match FastAPI,
    # but the server and code still work fine. So ignore PyCharm's warning:
    # noinspection PyTypeChecker
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
