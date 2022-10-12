# Docker Commands

## 1. docker ps
    List of all running containers.

***Example***

    docker ps
    docker ps -a        # -a or -all tag return all the containers irrespective of state.

>***Result:***


## 2. docker create
    Command is used to create container using docker image. It does not run the container. 

    Sntax   :   docker create <image_name>

***Example**

    dcker create --name alpine-container alpine

>***Result:***


## 3. docker start
    Command is used to start the container which is already created. 

    Syntax  :   docker start <docker_id or docker_name>

***Example***

    docker start alpine-container       # using containder name
    docker start 83703NSH*S234JSDJFWRF  # using container ID

>***Result:***


## 3. docker stop
    Command is used to stop the running container. 

    Syntax  :   docker stop <container_id or container_name>

***Example***

    docker container alpine-container

>***Result***


## 4. docker restart 
    Command is used to restart the container.

    Syntax  : docker restart <container_id or container_name>

***Example***

    docker stop alpine-container

>***Result:***



## 5. docker run
    Command is used to create and start container in one go. 

    syntax  :   docker run <image_name>

***Example**

    docker run nginx

>***Result:***


## 6. 