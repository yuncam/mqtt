# Base image
FROM alpine:latest

# Set environment variables
ARG MQTT_BROKER_IP
ENV MQTT_BROKER_IP=$MQTT_BROKER_IP

# Install dependencies and tools
# Runs before mounting starting the container and mounting any volumes
RUN apk add --no-cache python3 && \
    apk add --no-cache py3-pip && \
    pip3 install paho-mqtt

# Default command is executed after starting the container
CMD mkdir -p /home/scripts/ && \
    # Copy the scripts from the mounted volume to the /home/scripts directory
    cp -r /scripts /home/ && \
    # Change the IP address of the MQTT broker in the subscriber's config file
    sed -i "s/CHANGE_ME/$MQTT_BROKER_IP/g" /home/scripts/subscriber/config.py && \
    /bin/sh
