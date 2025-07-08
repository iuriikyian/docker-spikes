import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from loguru import logger

SHOW_OPENAPI = os.environ.get('SHOW_OPENAPI', 'false') == 'true'
logger.debug(f'SHOW_OPENAPI={SHOW_OPENAPI}')
PATH_PREFIX = os.environ.get('PATH_PREFIX', '')
PORT = os.environ.get('PORT', 8001)

from.routers.app_router import router as app_router, get_app_version

docsUrl = None
if SHOW_OPENAPI:
    docsUrl = f'{PATH_PREFIX}/docs'

app = FastAPI(
    title='docker entrypoint test',
    description='docker entrypoint test app',
    version=get_app_version(),
    openapi_url=f'{PATH_PREFIX}/openapi.json',
    docs_url=docsUrl
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # type:ignore[arg-type]
    allow_credentials=True, # type:ignore[arg-type]
    allow_methods=["GET", "POST"], # type:ignore[arg-type]
    allow_headers=["*"], # type:ignore[arg-type]
)

logger.info(f'started with api router prefix: {PATH_PREFIX}')
app.include_router(app_router, prefix=PATH_PREFIX, tags=['app'])