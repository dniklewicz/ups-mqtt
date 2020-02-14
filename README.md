# ups-mqtt

Simple python tool for fetching data from NUT server and publishing output to MQTT server.\
Can be used for UPS connected to Synology NAS with UPS Network Server Enabled.

Configuration via docker's environment variables.\
If used with Synology UPS Network Server, please remember to add Docker's IP address to the whitelist.

## Environment variables:
`UPS_HOST` - address of NUT server\
`MQTT_TOPIC` - base MQTT topic\
`MQTT_HOST` - address of MQTT server\
`MQTT_USERNAME` - MQTT username\
`MQTT_PASSWORD` - MQTT password\
`INTERVAL` - polling interval in seconds

## Networking
If you want to get the same IP address for your docker container between restarts, you can create new docker network with limited address space:
```
Subnet mask: 172.xx.0.0/30
IP range: 172.xx.0.0/30
Gateway: 172.xx.0.1
```
Then your container should use address `172.xx.0.2`.

Use at your own risk. No warranty provided.
