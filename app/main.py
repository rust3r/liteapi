from contextlib import asynccontextmanager

from litestar import Litestar
from litestar.di import Provide
from litestar.config.cors import CORSConfig
from litestar.openapi import OpenAPIConfig
from litestar_granian import GranianPlugin

from app.db.session import db_plugin
from app.controllers.user import UserController
from app.service.user import provide_user_service, provide_limit_offset_pagination


@asynccontextmanager
async def lifespan(app: Litestar):
    yield


cors_config = CORSConfig(allow_origins=["*"])

app = Litestar(
    route_handlers=[UserController],
    plugins=[GranianPlugin(), db_plugin],
    openapi_config=OpenAPIConfig(
        title="Lite API",
        version="1.0.0",
        description="API for managing users",
    ),
    cors_config=cors_config,
    dependencies={
        "service": Provide(provide_user_service),
        "limit_offset": Provide(provide_limit_offset_pagination),
    },
    lifespan=[lifespan],
)