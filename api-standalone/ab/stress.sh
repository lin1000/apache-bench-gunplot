
#Sample Usage
#./stress.sh 1000 10 http://localhost:9090/api_view

#Read CLI arguments first
#STRESS_TOTAL_REQUEST is a number
STRESS_TOTAL_REQUEST=$1
#STRESS_CONCURRENCY is a number
STRESS_CONCURRENCY=$2
#STRESS_URL is a url
STRESS_URL="$3"
STRESS_URL_FILENAME=$(echo $STRESS_URL | sed 's/[^a-zA-Z0-9]/_/g')

STRESS_RESULT_FILENAME="ab-results/${STRESS_URL_FILENAME}-${STRESS_TOTAL_REQUEST}-${STRESS_CONCURRENCY}.tsv"
STRESS_RESULT_GRAPH1_FILENAME="graphs/${STRESS_URL_FILENAME}-${STRESS_TOTAL_REQUEST}-${STRESS_CONCURRENCY}.png"
STRESS_RESULT_GRAPH2_FILENAME="graphs/${STRESS_URL_FILENAME}-${STRESS_TOTAL_REQUEST}-${STRESS_CONCURRENCY}-sorted.png"

#Source required project evn shells
#None

#Run main task
ab -r -n ${STRESS_TOTAL_REQUEST} -c ${STRESS_CONCURRENCY} -g "${STRESS_RESULT_FILENAME}" ${STRESS_URL}

#RUN A TEST AND GNUPLOT 2 GRAPHS
./plot-ab-tsv.sh "${STRESS_RESULT_FILENAME}" "${STRESS_RESULT_GRAPH1_FILENAME}" "Stress Testing ${STRESS_TOTAL_REQUEST}/${STRESS_CONCURRENCY} on ${STRESS_URL}"
./plot-ab-tsv-sorted.sh "${STRESS_RESULT_FILENAME}" "${STRESS_RESULT_GRAPH2_FILENAME}" "Stress Testing ${STRESS_TOTAL_REQUEST}/${STRESS_CONCURRENCY} on ${STRESS_URL}"