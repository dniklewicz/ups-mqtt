# ups-mqtt

Simple python tool for fetching data from NUT server and publishing output to MQTT server.\
Can be used for UPS connected to Synology NAS with UPS Network Server Enabled.

Configuration via file `/opt/app/conf/config.ini`.\
If used with Synology UPS Network Server, please remember to add container's IP address to the whitelist.

## Default configuration file:
```
[UPS]
# Address of NUT server
#hostname=localhost

[MQTT]
# Base MQTT topic
#base_topic=home/ups

# Address of MQTT server
#hostname=localhost

# MQTT server port
#port=1883

# MQTT username
#username=

# MQTT password
#password=

[General]
# Polling interval in seconds
#interval=60
```

## Networking
If you want to get the same IP address for your docker container between restarts, you can create new docker network with limited address space:
```
Subnet mask: 172.xx.0.0/30
IP range: 172.xx.0.0/30
Gateway: 172.xx.0.1
```
Then your container should use address `172.xx.0.2`.

Use at your own risk. No warranty provided.
