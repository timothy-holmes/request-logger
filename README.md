# request-logger

Records requests to server. Opportunity to turn this into middleware for hosted web apps to assist with debugging.

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
    cat $(ls ./data)
```

4. Wait for the requests (droids) you're looking for...