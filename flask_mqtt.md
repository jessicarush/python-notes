# Flask-mqtt

See the [flask-mqtt documentation](https://flask-mqtt.readthedocs.io/en/latest/api/index.html)  
See also: [MQTT Essentials](https://www.hivemq.com/blog/mqtt-essentials-part-4-mqtt-publish-subscribe-unsubscribe/)

## Table of contents

<!-- toc -->

- [Introduction](#introduction)
- [Install](#install)
- [Instantiate and include](#instantiate-and-include)
- [Client side](#client-side)
- [Server side](#server-side)
- [Notes](#notes)

<!-- tocstop -->

## Introduction

MQTT is a lightweight, publish-subscribe network protocol that transports messages between devices using an MQTT broker.

A client can publish messages as soon as it connects to a broker. Each message contains a topic that the broker uses to forward the message to interested clients. To receive messages on topics, a client sends a subscribe message to the MQTT broker.

When a client sends a message to an MQTT broker for publication, the broker reads the message, acknowledges it (according to the Quality of Service [QoS] Level), and sends it off to the clients who have subscribed to the topic.

The client that initially publishes the message is only concerned about delivering the message to the broker. Once the broker receives the message, it is the responsibility of the broker to deliver the message to all subscribers. The publishing client does not get any feedback about whether anyone is interested in the published message or how many clients received the message from the broker.

## Install

```
pip install flask-mqtt
```

## Instantiate and include

`__init__.py`
```python
from flask_mqtt import Mqtt

app = Flask(__name__)
mqtt = Mqtt(app, connect_async=True)  # To address flask-mqtt issue #73
```

`run.py`
```python
socketio.run(app,
             host='0.0.0.0',
             port=80,
             debug=True,
             use_reloader=False,  # mqtt requires this
             certfile='cert.pem',
             keyfile='key.pem')
```

`routes.py`
```python
from app import mqtt
```

`config.py`
```python
# MQTT configuration variables
MQTT_BROKER_URL = 'localhost'
MQTT_BROKER_PORT = 1883
MQTT_USERNAME = ''
MQTT_PASSWORD = ''
MQTT_KEEPALIVE = 10
MQTT_TLS_ENABLED = False
```

See the [flask-mqtt docs](https://flask-mqtt.readthedocs.io/en/latest/configuration.html#configuration-keys) for a complete list of the config keys.

## Client side

All socketio

## Server side

```python
# subscribe to a topic as soon as mqtt is connected
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('home/mytopic')

# handle the subscribed messages
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )

# unsubscribe
mqtt.unsubscribe('home/mytopic')
mqtt.unsubscribe_all()

# publish a message
mqtt.publish('home/mytopic', 'this is my message')
```

## Notes

- A subscribe message can contain multiple subscriptions for a client. Each subscription is made up of a topic and a QoS level.

- The topic in the subscribe message can contain wildcards that make it possible to subscribe to a topic pattern rather than a specific topic.

- If there are overlapping subscriptions for one client, the broker delivers the message that has the highest QoS level for that topic.

-  The broker holds the session data of all clients that have persistent sessions, including subscriptions and missed messages.

- Published messages have a Retain Flag (true/false). This flag defines whether the message is saved by the broker as the last known good value for a specified topic. When a new client subscribes to a topic, they receive the last message that is retained on that topic.

- $ topics are reserved for internal statistics of the MQTT broker, for example:
  ```
  $SYS/broker/clients/connected
  $SYS/broker/clients/disconnected
  $SYS/broker/clients/total
  $SYS/broker/messages/sent
  $SYS/broker/uptime
  ```

- A retained message is a normal MQTT message with the retained flag set to true. Using retained messages helps provide the last good value to a connecting client immediately.

- The clean session flag tells the broker whether the client wants to establish a persistent session or not. In a persistent session (CleanSession = false), the broker stores all subscriptions for the client and all missed messages for the client that subscribed with a Quality of Service (QoS) level 1 or 2. If the session is not persistent (CleanSession = true), the broker does not store anything for the client and purges all information from any previous persistent session. Note in the Flask-MQTT github readme example, they have a config: `app.config['MQTT_CLEAN_SESSION'] = True` but this config is missing from the documentation.

- In MQTT, you use the Last Will and Testament (LWT) feature to notify other clients about an ungracefully disconnected client. Each client can specify its last will message when it connects to a broker. The last will message is a normal MQTT message with a topic, retained message flag, QoS, and payload. The broker stores the message until it detects that the client has disconnected ungracefully. In response to the ungraceful disconnect, the broker sends the last-will message to all subscribed clients of the last-will message topic. If the client disconnects gracefully with a correct DISCONNECT message, the broker discards the stored LWT message. Clients can specify an LWT message in the CONNECT message that initiates the connection between the client and the broker.
