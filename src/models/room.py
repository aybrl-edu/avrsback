from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER as Integer
from ..database import db


class Room(db.Model):
    __tablename__ = 'room'

    id_room = Column(Integer(unsigned=True), primary_key=True)
    capacity = Column(Integer, nullable=True)
    name = Column(String(10), nullable=True)
