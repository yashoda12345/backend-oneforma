from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.repository.base_repo import BaseRepository
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app import repository, models
from fastapi.encoders import jsonable_encoder


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create_user(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            first_name=obj_in.first_name,
            last_name=obj_in.last_name,
            email=obj_in.email,
            password=get_password_hash(obj_in.password),
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_user(self, db: Session, db_user: models.User, update_data: dict):
        for key, value in update_data.dict().items():
            setattr(db_user, key, value) if value else None
        db.commit()
        db.refresh(db_user)
        return db_user

    # db_obj = db.query(User).filter(User.id == current_user.id).update(update_data)
    # db.commit()
    # db.refresh(db_obj)
    # return db_obj

    # def update(
    #         self, db: Session, *, db_obj: User, current_user: models.User, obj_in: Union[UserUpdate, Dict[str, Any]]
    #
    # ) -> User:
    #
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     return super().update(db, db_obj=db_obj, obj_in=update_data, current_user=current_user)

    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = UserRepository(User)
