## __Starting the docker container manually__
### Run mqtt-broker MQTT container:
```
docker run --name mqtt-broker --hostname=8b6c8703a75d --mac-address=02:42:ac:11:00:02 --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --env=VERSION=2.0.15 --env=DOWNLOAD_SHA256=4735b1d32e3f91c7a8896741d88a3022e89730a1ee897946decfa0df27039ac6 --env=GPG_KEYS=A0D6EEA1DCAE49A635A3B2F0779B22DFB3E717B7 --env=LWS_VERSION=4.2.1 --env=LWS_SHA256=842da21f73ccba2be59e680de10a8cce7928313048750eb6ad73b6fa50763c51 --volume=mqtt_data:/mosquitto/data --volume=mqtt_config:/mosquitto/config --volume=mqtt_log:/mosquitto/log -p 1883:1883 --restart=no --label='description=Eclipse Mosquitto MQTT Broker' --label='maintainer=Roger Light <roger@atchoo.org>' --runtime=runc -d eclipse-mosquitto
```

>   ### Change content of /mosquitto/config/mosquitto.conf to:
>   ```
>   persistence true
>   persistence_location /mosquitto/data/
>   user mosquitto
>   listener 1883
>   allow_anonymous true
>   log_dest file /mosquitto/log/mosquitto.log
>   log_dest stdout
>   ```

### Run mqtt-client-01 Alpine container:
```
docker run -ti --name mqtt-client01 --hostname=c2b6b137cfa2 --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --volume=mqtt_client_01:/home/mqtt_client_01/ --runtime=runc -d alpine:latest
```

### Run mqtt-client-01 Ubuntu container:
```
docker run -ti --name mqtt-client01 --hostname=c2b6b137cfa2 --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin --volume=mqtt_client_01:/home/mqtt_client_01/ --runtime=runc -d ubuntu:latest
```

<br><br>

## __After container is started__
### MQTT Broker (Alpine) Dependencies/Commands:
```
apk add --no-cache python3
apk add --no-cache py3-pip
pip3 install paho-mqtt
```

### Client (Alpine) Dependencies/Commands:
```
apk add python3 --no-cache
apk add py3-pip --no-cache
pip3 install paho-mqtt
```

### Client (Ubuntu) Dependencies/Commands:
```
apt install python3
apt install python3-pip
python3 -m pip install paho-mqtt
[opt] apt install mosquitto
[opt] apt install systemctl
[opt] systemctl start mosquitto
[opt] apt install iputils
[opt] apt install iproute2
[opt] apt install nano
```

<br><br>

## __Create shared network between containers__
This short tutorial shows how to create a shared network in docker so the containers can communicate with each other
using the example of two apache-php containers and the network 'myNetwork'. 
(Needles to say) you have to change the parameters according to your project.

### Create two containers:
```
docker run -d --name web1  -p 8001:80 eboraas/apache-php
docker run -d --name web2  -p 8002:80 eboraas/apache-php
```
> Important note: it is very important to explicitly specify a name with --name for your containers otherwise I’ve noticed that it would not work with the random names that Docker assigns to your containers.

### Then create a new network:
```
docker network create myNetwork
```

### After that connect your containers to the network:
```
docker network connect myNetwork web1
docker network connect myNetwork web2 
```

### Check if your containers are part of the new network:
```
docker network inspect myNetwork
```

### Then test the connection:
```
docker exec -ti web1 ping web2
```

<br><br>

## __Docker commands__
### Compose and start the containers:
```docker-compose up -d```  

### Stop and remove the containers:
```docker-compose down```  

### Access a Docker container shell:
```docker exec -it <CONTAINER_NAME_OR_ID> /bin/sh```
> ### Examples:   
> ```docker exec -it mqtt-client-1 /bin/sh```   
> ```docker exec -it mqtt-broker-1 /bin/sh```

### Remove unused builder resources and dangling builder cache:
```docker builder prune```

<br><br>

## __Using the scripts__
- First you want to [compose the docker containers](#compose-and-start-the-containers)
- Connect to the container shells via Docker Desktop GUI or via [shell](#access-a-docker-container-shell)
- Then execute the corresponding python scripts:

#### On broker:
```python3 /home/scripts/publisher/prompt_publisher.py```

#### On client:
```python3 /home/scripts/subscriber/subscriber.py```
> The broker IP must be changed in /home/scripts/subscriber/config.py accordingly!


