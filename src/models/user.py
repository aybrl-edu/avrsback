from sqlalchemy import Column, String, SmallInteger, LargeBinary
from sqlalchemy.dialects.mysql import INTEGER as Integer
from ..database import db


class User(db.Model):
    __tablename__ = 'users'

    id_user = Column(Integer(unsigned=True), primary_key=True)
    email = Column(String(40), nullable=True)
    enrolled = Column(SmallInteger, nullable=True)
    picture = Column(LargeBinary, nullable=True)
    firstname = Column(String(20), nullable=True)
    lastname = Column(String(20), nullable=True)
    picture2 = Column(LargeBinary, nullable=True)
    photo = Column(LargeBinary, nullable=True)

    def to_dict(self):
        return {
            'id_user': self.id_user,
            'email': self.email,
            'enrolled': self.enrolled,
            'firstname': self.firstname,
            'lastname': self.lastname,
        }
