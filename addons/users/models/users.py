from sqlalchemy import Column, String, Integer

from ferp.db.base_class import Base
from ferp.db.crud import CRUDBase

from ..schemas.users import UserCreate, UserUpdate


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)


class CRUDItem(CRUDBase[User, UserCreate, UserUpdate]):
    def login_with_username(self, username, login):
        ...

    def login_with_email(self, email, login):
        ...


user = CRUDItem(User)
