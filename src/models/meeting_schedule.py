from sqlalchemy import Column, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text
from sqlalchemy.dialects.mysql import INTEGER as Integer
from ..database import db


class MeetingSchedule(db.Model):
    __tablename__ = 'meeting_schedule'

    id_meeting = Column(Integer(unsigned=True), primary_key=True)
    id_organisator = Column(Integer, ForeignKey('users.id_user'), nullable=True)
    id_room = Column(Integer, ForeignKey('room.id_room'), nullable=True)
    date = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    duration = Column(Integer, nullable=True)

    room = relationship('Room', backref='meeting_schedules')
    organisator = relationship('User', backref='meeting_schedules')

    def to_dict(self):
        return {
            'id_meeting': self.id_meeting,
            'date': self.date,
            'duration': self.duration
        }
