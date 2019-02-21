source ../setenv.sh
echo Running docker-compose build

# ONLY NEED TO BUILD AT SERVICE LEVEL
docker-compose build
docker-compose push


# DONT NEED TO BUILD AT ROLE LEVEL 
# ROLE_DIR=role
# for dir in `ls $ROLE_DIR`;
# do
#     cd $ROLE_DIR/$dir;
#     pwd;
#     docker-compose build;
#     docker-compose push;
#     cd ../../;
# done
