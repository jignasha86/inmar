# inmar

## This is API server based on python-django framework

### Pre-requisites
    1) Python 2.7
    2) Mysql database
    
## Steps to setup with docker
   1) Install docker and docker-compose if not 
   2) Create new dir & change to that eg, mkdir test && cd test
   3) git clone https://github.com/jignasha86/inmar.git
   4) mv Dockerfile & docker-compose.yml outside of inmar repo
      eg, mv inmar/Dockerfile . && mv inmar/docker-compose.yml .
   5) run **dokcer-compose up -d mysql**
   6) run **docker-compose up -d web**
   
### Open http://localhost:3001/docs or http://{ip}:3001/docs in browser, to view apis documentation

#### If backend dont have any data, then new data can be imported by running below commands
     1) **docker exec -it docker_web_1 /bin/bash**
     2) http -f POST http://localhost:3001/api/v1/importdata file@Data.csv
     

    
 
