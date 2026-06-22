from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings
from app.core.lifespan import lifespan
from app.utils.system import (
    get_uptime,
    get_timestamp
)
from app.middleware.token_rotation import (
    TokenRotationMiddleware
)
from app.middleware.cors import (
    setup_cors
)
from app.exceptions import (
    register_exception_handlers
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)


setup_cors(app)
register_exception_handlers(app)
app.add_middleware(
    TokenRotationMiddleware
)



@app.get("/")
async def root():
    return {
        "message": "Rubel Mart's server is up and running...", 
        "success": True, 
        "status_code": 200,
        "data": {
            "uptime": (
                f"{get_uptime()} seconds"
            ),
            "timestamp": (
                get_timestamp()
            )
        }
    }

@app.get("/health")
async def health():
    return {
        "message": "Healthy",
        "success": True,
        "status_code": 200,
        "data": {
            "uptime": (
                f"{get_uptime()} seconds"
            ),
            "timestamp": (
                get_timestamp()
            )
        }
    }


app.include_router(api_router)