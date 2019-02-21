
#Prepare the environment
CURRENT_DIR=`pwd`
cd .. && source ./up-machine.sh
cd $CURRENT_DIR

#Call each up.sh in role folder
ROLE_DIR=role

for dir in `ls $ROLE_DIR`;
do
    cd $ROLE_DIR/$dir;
    ./up.sh;
    cd ../../;
done
