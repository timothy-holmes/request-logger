# request-logger

Records requests to server. Originally used to capture data from Shelly H&T sensor while smart home app on home server was non-functional. It gave me a bit of insight into how uvicorn worked. I might adapt it in the future to assist with debugging my web apps.

## To use, follow these steps:
1. Clone to host
```
    cd /srv/git
    git clone https://github.com/timothy-holmes/request-logger
```

2. Build and run using docker-compose
```
    cd request-logger
    docker-compose build
    docker-compose up -d
```

3. Test app
```
    curl http://192.168.1.103:80?parameter1=100&parameter2=200&parameter3=hahahaha
    cat *
```

4. Wait for the requests (droids) you're looking for...
