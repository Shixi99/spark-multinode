## Configure Spark standalone cluster on Docker

[Read detailed artice on medium](https://shixieyyub.medium.com/dockerd%C9%99-spark-standalone-cluster-qurulmas%C4%B1-2bca5410daf7)

### To run this project on your local machine:

Make sure you have **Docker Desktop**, **git** and **Make** installed on your computer

Open 2 terminals

In the first terminal run commands below
```bash
mkdir my_park_project
```
```
cd my_spark_project
```
```
git clone https://github.com/Shixi99/spark-multinode.git
```
```
cd spark-multinode
```
```
make run-scaled
```

In the second terminal
```bash
cd myproject\spark-multinode
```
```
make run submit app=sales.py
```

To down containers 
```bash
make down
```

