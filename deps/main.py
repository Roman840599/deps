import logging
import uvicorn

from fastapi import FastAPI

from custom_logging.custom_logging import CustomizeLogger
from v1.routers import documents


logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title='Deps', debug=True)
    logger = CustomizeLogger.make_logger()
    app.logger = logger
    return app


app = create_app()

app.include_router(documents.router)


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
