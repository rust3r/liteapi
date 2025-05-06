from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession
from litestar.repository.filters import LimitOffset
from litestar.params import Parameter

from app.db.models import User

class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = UserRepository


async def provide_user_service(db_session: AsyncSession) -> UserService:
    return UserService(session=db_session)


async def provide_limit_offset_pagination(
    current_page: int = Parameter(ge=1, query="currentPage", default=1, required=False),
    page_size: int = Parameter(
        query="pageSize",
        ge=1,
        default=10,
        required=False,
    ),
) -> LimitOffset:
    return LimitOffset(page_size, page_size * (current_page - 1))