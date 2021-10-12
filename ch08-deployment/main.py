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
    configure_fake_data()


def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
        raise Exception("settings.json file not found, you cannot continue, please see settings_template.json")

    with open('settings.json') as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get('api_key')


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure_fake_data():
    # This was added to make it easier to test the weather event reporting
    # We have /api/reports but until you submit new data each run, it's missing
    # So this will give us something to start from.
    pass  # Doesn't work on Ubuntu under gunicorn
    # try:
    #     loc = Location(city="Portland", state="OR", country="US")
    #     asyncio.run(report_service.add_report("Misty sunrise today, beautiful!", loc))
    #     asyncio.run(report_service.add_report("Clouds over downtown.", loc))
    # except:
    #     print("NOTICE: Add default data not supported on this system (usually under uvicorn on linux)")


if __name__ == '__main__':
    configure()
    # uvicorn was updated, and it's type definitions don't match FastAPI,
    # but the server and code still work fine. So ignore PyCharm's warning:
    # noinspection PyTypeChecker
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
