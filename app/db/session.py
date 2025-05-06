import os
from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig, SQLAlchemyPlugin, AsyncSessionConfig

from app.db.models import User

db_username = os.getenv("POSTGRES_USER", "postgres")
db_password = os.getenv("POSTGRES_PASSWORD", "postgres")
db_name = os.getenv("POSTGRES_DB", "liteapi")
db_port = os.getenv("POSTGRES_PORT", 5432)
db_host = os.getenv("DB_HOST", "localhost")

session_config = AsyncSessionConfig(expire_on_commit=False)
db_config = SQLAlchemyAsyncConfig(
    connection_string=f"postgresql+asyncpg://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}",
    session_config=session_config,
    metadata=User.metadata,
    create_all=True,
)

db_plugin = SQLAlchemyPlugin(config=db_config)