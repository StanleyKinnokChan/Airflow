# Apache Airflow Tutorial Series [YouTube](https://www.youtube.com/watch?v=z7xyNOF8tak&list=PLwFJcsJ61oujAqYpMp1kdUBcPG0sE0QMT)

This repository is for learning Airflow. Different from this is modified version using Apache airflow 2.8.3 in docker with local executor.

Here are the steps to take to get airflow running with docker on your machine. 
1. Clone this repo
2. Create dags, logs and plugins folder inside the project directory
```bash
mkdir ./dags ./logs ./plugins
```
3. Set user permissions for Airflow to your current user
```
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```
4. Install docker desktop application if you don't have docker running on your machine
- [Download Docker Desktop Application for Mac OS](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
- [Download Docker Desktop Application for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
5. Launch airflow by docker-compose
```bash
docker-compose up -d
```
6. Check the running containers
```bash
docker ps
```
7. Open browser and type http://localhost:8080 to launch the airflow webserver
