from sqlalchemy import Column, String, Integer

from db.base_class import Base


class Group(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
