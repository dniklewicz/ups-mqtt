FROM python:3-slim

RUN apt-get update && apt-get install -y nut-client
RUN pip install --no-cache-dir paho-mqtt

RUN mkdir -p /opt/app/conf

WORKDIR /opt/app

COPY config.ini ./

ADD ups-mqtt.py ./

CMD ["python", "ups-mqtt.py"]