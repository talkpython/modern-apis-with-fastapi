import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate(x: int, y: int, z: int = 10):
    value = (x + y)*z

    return {
        'value': value
    }


uvicorn.run(api, port=8000, host="127.0.0.1")
