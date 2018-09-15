
#Sample Usage
#./plot-ab-tsv.sh ab-results/ab-test-1.tsv graphs/test.png "Stress Testing"

#Read CLI arguments first
#GNUPLOT_INPUT_FILE_NAME is a tsv file
GNUPLOT_INPUT_FILE_NAME=$(pwd)/$1
#GNUPLOT_INPUT_FILE_NAME is a png file
GNUPLOT_OUTPUT_FILE_NAME=$(pwd)/$2
#GNUPLOT_INPUT_FILE_NAME is a png file
GNUPLOT_TITLE="$3"

#Source required project evn shells
#workdirectory where the script was initiated=$(pwd)
#relative form of pwd =$(dirname $BASH_SOURCE)/
#absolute form of pwd =$(pwd)/$(dirname $BASH_SOURCE)/
source $(dirname $BASH_SOURCE)/../setenv.sh

#Run main task
"$GNUPLOT_PRJ_HOME/bin/plot-ab-tsv-sorted.sh" "${GNUPLOT_INPUT_FILE_NAME}" "${GNUPLOT_OUTPUT_FILE_NAME}" "${GNUPLOT_TITLE}"