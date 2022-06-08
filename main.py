from uvicorn.main import run
from logging import getLogger

from app.api import app as application

logger = getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting API port 8000")
    run("main:application", host="0.0.0.0", port=8000, workers=1, reload=True)
