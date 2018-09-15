
#Whether the script was executed or sourced
# if [ "$0" == "$BASH_SOURCE" ]; then
# 	#if this script was sourced
# 	echo "executed version .."
# 	echo $0
#     echo $(dirname $BASH_SOURCE)
# else
# 	#if this script was executed directly
# 	echo "sourced version .. "
#     echo $0
#     echo $BASH_SOURCE
#     echo $(pwd)/$(dirname $BASH_SOURCE)/
# fi
export GNUPLOT_PRJ_HOME="$(pwd)/$(dirname $BASH_SOURCE)/gnuplot"