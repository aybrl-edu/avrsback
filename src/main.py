from flask import jsonify

from src import create_app
from worker import reservation_worker
from worker import get_available_parking_slots

app = create_app()

# MQTT broker information
broker_url = 'eaab39b7e7aa4673b3f2ae49452a32e9.s2.eu.hivemq.cloud'
broker_port = 8883
client_id = 'python-flask-client'
username = 'python'
password = 'python42'
topic = 'place/status'

# Create an instance of the MqttClient class
# mqtt_client = MqttClient(broker_url, broker_port, client_id, username, password, topic)


@app.route('/api/parking_slots', methods=['GET'])
def get_parking_slots():
    # Return the available parking slots as JSON
    return get_available_parking_slots()


@app.route('/api/users', methods=['GET'])
def get_users():
    # Return users
    return jsonify(reservation_worker())


if __name__ == '__main__':
    app.run(debug=True)
