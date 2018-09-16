
#Whether the script was executed or sourced
# if [ "$0" == "$BASH_SOURCE" ]; then
# 	#if this script was executed directly
# 	echo "executed version .."
# 	source $(dirname $BASH_SOURCE)/../setenv.sh
# 	#pwd=$(pwd) && cd .. && source "./setenv.sh" && basename "$0" && cd ${pwd}
# else
# 	#if this script was sourced
# 	echo "sourced version .. "
# 	source $(dirname $BASH_SOURCE)/../setenv.sh
# fi
source $(dirname $BASH_SOURCE)/../setenv.sh


# $1 is openapi.merge=[true or false]
function gradlew_bootJar(){
	./gradlew bootJar -Popenapi.merge=$1
}

# $1 is openapi.merge=[true or false]
function gradlew_compile_and_merge(){
	./gradlew clean compileJava -Popenapi.merge=$1
}

# $1 is service name
# $2 is version
function docker_build(){
	docker build . -t $1:$2 \
	--build-arg SRC_JAR_FILE=build/libs/$1-$2.jar \
	--build-arg SERVICE_JAR_FILE_NAME=service.jar
}

# $1 is service name
# $2 is version
# $3 is target_registery_url
# $4 is target_registery namespace
function docker_tag(){
	docker tag $1:$2 $3/$4/$1:$2
}

# $1 is service name
# $2 is version
# $3 is target_registery_url
# $4 is target_registery namespace
function docker_push(){
	docker push $3/$4/$1:$2
}


# $1 is service name
# $2 is version
# $3 is node port
# $4 is container expose port
function docker_run_local(){
	docker_rm $1-local
	docker run --name $1-local -d -p $3:$4 -v "$(pwd)/$(dirname $BASH_SOURCE)/data:/app/data" $1:$2 	
}

# $1 is container_name
function docker_rm(){
	docker rm -f $1
}


red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`