<!-- Python application hosted on a NGNX Server -->
# Instructions
This project is to show how to host an application in a remote server such as NGINX 
Steps:
1. Clone this repository
2. Use Docker compose up to kick off a docker container and image
3. Verify that the container is created: docker ps 
4. Run the container : docker run + container name (or container ID)
    I advice to allocate a port in the range 80-82 port:

       ```docker run -d -p 8180:80 makeapie_docker-devcontainer```


    8180--> This is where our application will be located, it refers to the Docker Container
    80----> This refers to the location in our local. 
5. Go to http://localhost:8180/
6. You should get a greeting NGINX server on screen
7. Add main.py to localhost and confirm it downloads main.py file
