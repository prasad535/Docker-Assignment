# Docker Commands

## 1. docker ps
    List of all running containers.

***Example***

    docker ps
    docker ps -a        # -a or -all tag return all the containers irrespective of state.

>***Result:***
![](/./Screenshots/ps.png)


## 2. docker create
    Command is used to create container using docker image. It does not run the container. 

    Sntax   :   docker create <image_name>

***Example**

    dcker create --name alpine-container alpine

>***Result:***
![](/./Screenshots/create.png)

## 3. docker start
    Command is used to start the container which is already created. 

    Syntax  :   docker start <docker_id or docker_name>

***Example***

    docker start alpine-container       # using containder name
    docker start 83703NSH*S234JSDJFWRF  # using container ID

>***Result:***
![](/./Screenshots/2022-10-18-00-27-39.png)

## 3. docker stop
    Command is used to stop the running container. 

    Syntax  :   docker stop <container_id or container_name>

***Example***

    docker container alpine-container

>***Result***
![](/./Screenshots/2022-10-18-00-26-23.png)

## 4. docker restart 
    Command is used to restart the container.

    Syntax  : docker restart <container_id or container_name>

***Example***

    docker stop alpine-container

>***Result:***
![](/./Screenshots/restart.png)


## 5. docker run
    Command is used to create and start container in one go. 

    syntax  :   docker run <image_name>

***Example**

    docker run nginx

>***Result:***
![](/./Screenshots/2022-10-18-00-29-43.png)

## 6. docker rm 
    Command is used to remove containers

    Syntax : docker rm <container_name>

***Example***

    docker rm nginx

>***Result:***
![](/./Screenshots/2022-10-18-00-30-26.png)

## 7. docker images
    Command is used to list the all the images

    Syntax : docker images

***Example***

    docker images

>***Result***
![](/./Screenshots/2022-10-18-00-15-34.png)
## 8. docker rmi 
    Command is used to remove the images

    syntax  :   docker rmi <image_name>

***Example***

    docker image alpine

>***Result:***
![](/./Screenshots/2022-10-18-00-31-47.png)

## 9. docker pull
    Command is used to download the image locally. 

    Syntax  : docker pull <image_name>

***Example***

    docker pull redis

>***Result***
![](/./Screenshots/2022-10-18-00-32-51.png)

## 10. docker push
    Command is used to push the image to docker repository.

    Syntax  :   docker push image

***Example***

    docker push image_name

>***Result***
![](/./Screenshots/2022-10-18-00-34-25.png)