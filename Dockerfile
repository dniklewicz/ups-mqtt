FROM python:3-slim

RUN apt-get update && apt-get install -y nut-client
RUN pip install --no-cache-dir paho-mqtt

ADD ups-mqtt.py ./

ENV MQTT_TOPIC=home/ups
ENV UPS_HOST=localhost
ENV MQTT_HOST=localhost
ENV MQTT_PORT=1883
ENV MQTT_USERNAME=
ENV MQTT_PASSWORD=
ENV INTERVAL=60

CMD ["python", "./ups-mqtt.py"]