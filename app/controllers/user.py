from litestar import Controller, get, post, put, delete
from litestar.pagination import OffsetPagination
from litestar.repository.filters import LimitOffset
from litestar.params import Parameter

from app.dto.user import UserCreate, UserUpdate, UserOut, UserDTO
from app.service.user import UserService


class UserController(Controller):
    path = "/users"
    tags = ["users"]
    return_dto = UserDTO

    @post(
            summary="Create new user"
    )
    async def create_user(
        self,
        service: UserService,
        data: UserCreate,
    ) -> UserOut:
        user = await service.create(data.model_dump())
        await service.repository.session.commit()
        return user

    @get(
            summary="Retrieve all users"
    )
    async def list_users(
        self,
        service: UserService,
        limit_offset: LimitOffset,
    ) -> OffsetPagination[UserOut]:
        results, total = await service.list_and_count(limit_offset)
        return OffsetPagination[UserOut](
            items=results,
            total=total,
            limit=limit_offset.limit,
            offset=limit_offset.offset,
        )

    @get(
            path="/{user_id:int}",
            summary="Retrieve user by ID"
    )
    async def get_user(
        self,
        service: UserService,
        user_id: int = Parameter(title="User ID", description="ID user to retrieve"),
    ) -> UserOut:
        return await service.get(user_id)

    @put(
            path="/{user_id:int}",
            summary="Update user by ID"
    )
    async def update_user(
        self,
        service: UserService,
        data: UserUpdate,
        user_id: int = Parameter(title="User ID", description="ID user to update"),
    ) -> UserOut:
        user = await service.update(data.model_dump(exclude_unset=True), item_id=user_id)
        await service.repository.session.commit()
        return user

    @delete(
            path="/{user_id:int}",
            summary="Delete user by ID"
    )
    async def delete_user(
        self,
        service: UserService,
        user_id: int = Parameter(title="User ID", description="ID user to delete"),
    ) -> None:
        await service.delete(user_id)
        await service.repository.session.commit()