import paho.mqtt.client as mqtt
import ssl
import threading
from config import parking_data

class MqttClient:
    def __init__(self, broker_url, broker_port, client_id, username, password, topic):
        self.broker_url = broker_url
        self.broker_port = broker_port
        self.client_id = client_id
        self.username = username
        self.password = password
        self.topic = topic

        # MQTT client information
        self.ca_cert = 'certificate.pem'

        # Create an MQTT client instance
        self.client = mqtt.Client(self.client_id)
        self.client.username_pw_set(self.username, self.password)
        self.client.tls_set(self.ca_cert, tls_version=ssl.PROTOCOL_TLSv1_2)

        # Set the callback functions for MQTT events
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Start the MQTT client loop in a separate thread
        self.thread = threading.Thread(target=self.start_mqtt_client)
        self.thread.start()

    def on_connect(self, client, userdata, flags, rc):
        print('Connected to MQTT broker with result code ' + str(rc))
        # Subscribe to the MQTT topic
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode('utf-8').split(' : ')
        place_id = int(message[0])
        parking_data[place_id] = int(message[1])

    def start_mqtt_client(self):
        self.client.connect(self.broker_url, self.broker_port)
        self.client.loop_forever()

    def stop_mqtt_client(self):
        self.client.disconnect()
        self.thread.join()
