from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return "docker entrypoint test server"

@router.get("/health", description='Service health check endpoint')
def health() -> str:
    return 'healthy'

_appVersion = None

def get_app_version() -> str:
    global _appVersion
    if _appVersion is None:
        with open('VERSION', 'r') as fin:
            _appVersion = fin.read()
    return _appVersion

@router.get("/version", description='Versions info')
def get_version() -> dict[str, str]:
    return dict(
        appVersion=get_app_version()
    )
