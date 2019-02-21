# api-study
Study of API Performane

## How to generate doc
```bash
cd api-standalone/doc
make clean && make html
```


## How to start up docker-compose containers
專案目錄的安排 :
* 外層的 docker-compose.yml 會一次啟動所有的container - 整合測試
* 個別服務的 docker-compose.yml 僅會啟動單一container - 單完測試（有些功能會無法運作)
```bash
docker-compose down && docker-compose build && docker-compose up -d
```


## Install Apache Benach
### CentOS
```bash
yum install httpd-tools
```
### Ubuntu
```bash
apt-get install apache2-utils
apt-get install gnuplot
```

ab -k -n 20000 -c 100 http://47.75.206.128:8090/
ab -k -n 20000 -c 200 http://47.75.206.128:8090/

ab -n 200 -c 100 -g ab-test.tsv http://130.198.90.185:8090/

ab -k -n 20 -c 1 http://130.198.90.185:8090/
ab -n 20 -c 1 http://130.198.90.185:8090/
ab -k -n 20000 -c 100 http://130.198.90.185:8090/
ab -k -n 20000 -c 100 http://130.198.90.185:8090/
ab -k -n 20000 -c 100 http://130.198.90.185:8090/
ab -k -n 20000 -c 200 http://130.198.90.185:8090/
ab -k -n 20000 -c 300 http://130.198.90.185:8090/
ab -k -n 20000 -c 400 http://130.198.90.185:8090/

```bash
#CD to api server folder and then ab subfolder
cd <api-service-folder>/ab

#RUN A TEST AND GNUPLOT 2 GRAPHS
ab -r -n 1000 -c 10 -g ab-results/130.198.90.185-1000-10.tsv http://130.198.90.185:8090/
./plot-ab-tsv.sh ab-results/130.198.90.185-1000-10.tsv graphs/130.198.90.185-1000-10.png "Stress Testing 1000/10"

#RUN A TEST AND GNUPLOT 2 GRAPHS
ab -r -n 100 -c 1 -g ab-results/130.198.90.185-100-1.tsv http://130.198.90.185:8090/
./plot-ab-tsv.sh ab-results/130.198.90.185-100-1.tsv graphs/130.198.90.185-100-1.png "Stress Testing 100/1"
./plot-ab-tsv-sorted.sh ab-results/130.198.90.185-100-1.tsv graphs/130.198.90.185-100-1-sorted.png "Stress Testing 100/1"

#RUN A TEST AND GNUPLOT 2 GRAPHS
ab -k -r -n 100 -c 1 -g ab-results/130.198.90.185-100-1.tsv http://130.198.90.185:8090/
./plot-ab-tsv.sh ab-results/130.198.90.185-100-1.tsv graphs/130.198.90.185-100-1-k.png "Stress Testing 100/1"
./plot-ab-tsv-sorted.sh ab-results/130.198.90.185-100-1.tsv graphs/130.198.90.185-100-1-sorted-k.png "Stress Testing 100/1"
```

```bash
#CD to api server folder and then ab subfolder
cd <api-service-folder>/ab

#RUN A TEST AND GNUPLOT 2 GRAPHS
ab -r -n 100 -c 10 -g ab-results/localhost-9090-100-10.tsv http://localhost:9090/api_view
./plot-ab-tsv.sh ab-results/localhost-9090-100-10.tsv graphs/localhost-9090-100-10.png "Stress Testing 100/10"
./plot-ab-tsv-sorted.sh ab-results/localhost-9090-100-10.tsv graphs/localhost-9090-100-10-sorted.png "Stress Testing 100/10"

./stress.sh 800 40 http://localhost:9090/api_view

```


# Curated list of Softwares
* API Stress Testing
    *   gnuplot : used to visualize ab result
    ```bash
    #install the gnuplot's dependency : qt
    brew update
    brew upgrade qt
    #install gnuplot on Mac using Homebrew
    brew install gnuplot --with-qt --with-x11
    ```
    ```bash
    #install the gnuplot's dependency : qt
    apt-get install gnuplot
    ```    

#GNUPLOT
[How To Run gnuplot example](http://research.physics.illinois.edu/ElectronicStructure/498-s97/comp_info/gnuplot.html)