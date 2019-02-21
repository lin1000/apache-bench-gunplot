source ./setenv.sh

docker_build nginx-edge-service 1.0.0
if [ $? -ne 0 ] 
then
    echo "${red}An error occured, please review why docker build failed.${reset}"
    exit 1
else
    echo "${green}Docker Build Succeed.${reset}"
fi