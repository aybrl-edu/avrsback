from threading import Timer
from src.models import User, MeetingSchedule, MeetingGuests


def reservation_worker():
    # Check reservation continuously

    users = MeetingSchedule.query.all()
    users_list = [user.to_dict() for user in users]
    return users_list


