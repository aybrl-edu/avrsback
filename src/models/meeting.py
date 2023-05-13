from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as Integer
from ..database import db


class MeetingGuests(db.Model):
    __tablename__ = 'meeting_guests'

    id = Column(Integer(unsigned=True), primary_key=True)
    id_meeting = Column(Integer, ForeignKey('meeting_schedule.id_meeting'), nullable=True)
    id_user = Column(Integer, ForeignKey('users.id_user'), nullable=True)

    meeting = relationship('MeetingSchedule', backref='guests')
    user = relationship('User', backref='meetings')

    def to_dict(self):
        return {
            'id_meeting': self.id_meeting,
            'id_user': self.id_user
        }
