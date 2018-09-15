source ./setenv.sh
docker_run_local api-standalone 1.0.0 8090 8081
if [ $? -ne 0 ] 
then
    echo "${red}An error occured, please review why docker run on local failed.${reset}"
    exit 1
else
    echo "${green}Docker Run on Local Succeed.${reset}"
fi