FROM python:3-slim

RUN apt-get update && apt-get install -y nut-client
RUN pip install --no-cache-dir paho-mqtt

WORKDIR /opt/app

COPY config.ini ./init/

ADD ups-mqtt.py ./

CMD ["python", "./ups-mqtt.py"]