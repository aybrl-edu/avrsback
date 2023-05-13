from src.config import parking_data
from flask import jsonify

parking_slots = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'C4', 'C5']


def get_parking_slots():
    print("hello")


def get_available_parking_slots():
    #return jsonify({'parking_slots': parking_slots})
    print(parking_data.count(0))
    slots = parking_data.count(0)
    return jsonify({'parking_slots': slots})


def make_reservation():
    print("hello")


def get_reservation():
    print("hello")