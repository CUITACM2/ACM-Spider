from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.models import BaseModel, session


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(255), unique=True, index=True, nullable=False)
    display_name = Column(String(255), index=True, nullable=False)
    password_digest = Column(String(1024))
    gender = Column(Boolean)
    avatar = Column(String(255))
    role = Column(Integer)
    status = Column(Integer, default=0)
    description = Column(String(1024))
    train_rank = Column(Integer)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self):
        pass

    def __repr__(self):
        return '<User {0}({1})>'.format(self.nickname, self.display_name)

    def save(self):
        self.updated_at = datetime.now()
        session.add(self)
        session.commit()
