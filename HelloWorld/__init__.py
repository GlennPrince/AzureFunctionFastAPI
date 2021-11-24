import logging
import azure.functions as func

from _future.azure.functions._http_asgi import AsgiMiddleware

import fastapi
app = fastapi.FastAPI()

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)


@app.get("/api/helloWorld")
async def get_helloWorld():
    return {
        "message": "This is a test message for Hello World"
    }