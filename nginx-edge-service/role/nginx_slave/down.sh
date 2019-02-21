echo Running docker-compose up with HOST_IP=$HOST_IP
echo Switching docker-machine env into edge 2
eval "$(docker-machine env edge2)" 
docker-compose down