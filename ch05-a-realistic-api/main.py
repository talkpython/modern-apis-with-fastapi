import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/')
def index():
    return "Hello Weather app!"


if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')
