from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, index=True, unique=True)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'))

    roles = relationship('Role', back_populates='users')


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    users = relationship('User', back_populates='roles')
