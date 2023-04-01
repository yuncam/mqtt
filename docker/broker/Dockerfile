# Base image
FROM eclipse-mosquitto:latest

# Install dependencies and tools
# Runs before mounting starting the container and mounting any volumes
RUN set -x && \
    apk add --no-cache python3 && \
    apk add --no-cache py3-pip && \
    pip3 install paho-mqtt

# Default command is executed after starting the container
CMD mkdir -p /home/scripts/ && \
    # Copy the scripts from the mounted volume to the /home/scripts directory
    cp -r /scripts /home/ && \
    # Start MQTT broker
    /usr/sbin/mosquitto -c /mosquitto/config/mosquitto.conf

