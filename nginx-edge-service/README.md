#NGNIX and lua as edge service 

## Docker Running Command


## Commands 

```bash
#build image using role/<role_name>/docker-compose.yml to build
./build.sh
#docker compose up roles
./up.sh
#docker compose down roles
./down.sh
```

```bash
export NGINX_LUA_HOME=$(pwd)
docker build -t nginx-edge-service .
docker rm -f nginx-edge-service
docker run --name nginx-edge-service -d \
    -v $NGINX_LUA_HOME/data/etc/nginx:/data/etc/nginx \
    -p 10080:80 \
    -p 10081:81 \
    nginx-edge-service
docker exec -it nginx-edge-service /bin/bash
docker logs nginx_lua_edge
#check whether amplify is running 
docker exec -it nginx_lua_edge /bin/bash
docker exec nginx_lua_edge ps axu
#check amplify log
docker exec nginx_lua_edge tail /var/log/amplify-agent/agent.log
docker exec nginx_lua_edge tail /var/log/nginx/access.log 
docker exec nginx_lua_edge tail /var/log/nginx/error.log 


# update nginx.conf and reload nginx
cp -f /data/etc/nginx/nginx.conf /etc/nginx/nginx.conf && \
nginx -s reload

/usr/sbin/nginx -c "/data/etc/nginx/nginx.conf" -t && \
    /usr/sbin/nginx -s reload -c "/data/etc/nginx/nginx.conf" -g "daemon off;"

# check how may clients and connections 
redis-cli CLIENT LIST | sed -n 's|.*addr=\(.*\)\:.*|\1|p' | sort | uniq -c
```

```
docker build -t 10.106.178.130:19999/nginx_lua_edge .
docker rm -f nginx_lua_edge
docker run --name nginx_lua_edge -d \
    -v $NGINX_LUA_HOME/etc/nginx:/data/etc/nginx \
    -p 10080:80 \
    -p 10081:81 \
    nginx_lua_edge 

```
