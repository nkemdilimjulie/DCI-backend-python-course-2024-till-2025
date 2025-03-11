# CLOUD - DOCKER - 04: Dockerize Django project

> Learning Goals
>- create and understand Dockerfiles
>- we will test the Image create by a custom Dockerfile
>- create a multi-container application using docker compose
>- first local testing auf this multi-container application
>- deployment of it on an ec2 instance


**Last Session**

- containers:
    - containers have a persistent nature
        - files that a save in a container and the container is stopped
            - the file remain in this container
            - it will be deleted if the container will be removed
- container running: `docker run image_name sleep 10`
- How long would the container be running? And why?
    - 10s
    - `sleep 10` is the main process that keeps the container alive
    - this process stops after 10s and therefore the container has not main command running anymore
        - and therefore the container stops running
- How does the `exec` command works:
- Purpose? 
    - run a command inside a *running* container
    - `docker exec django-container python manage.py migrate` 
- Container vs VM:
    - Hypervisors claim physical resources and 'simulate' hardware for the VM
    - each VM needs its own OS
    - Host shares its Kernel with containers
        - this makes container more efficient (less OS overhead)
            - and more lightweight
- self-healing:
    - in case a container shuts down
        - we can automatically restart the container
    - for this we use restart policies:
        - `-- restart always`
        - `-- restart on-failure`
        - `-- unless-stopped`


    - -- restart always restarts the container each time it stops; even if it shut down gracefully
    - -- restart on-failure restarts the container each time an error occurs; it crashes; you can add a number of times it will restart by adding :<num>
        - e.g. on-failure:3


# Multi-container apps with Compose

- we'll look at how to deploy multi-container applications using Docker Compose

## Deploying apps with Compose

- Modern cloud-native apps are made of multiple smaller services that interact to form a useful app.
- We call this the microservices pattern.
    - easier to maintain
        - if one service fails the rest still works
        - smaller services become more managable
        - better to test
        - each service as a responsibility
            - we have less coupling

A microservices app might have the following seven independent services that work together to form a useful application:

- Web front-end
- Ordering
- Catalog
- Back-end datastore
- Logging

Deploying and managing lots of small microservices like these can be hard.

- Docker Compose helps by simplifying the process with a declarative configuration file.
- Instead of using scripts and long Docker commands, Compose lets you describe everything in this configuration file.
- The configuration file can be used to deploy and manage your microservices.
- Once deployed, you can manage the entire lifecycle of your app with a simple set of commands.
- The configuration file can also be stored and managed in a version control system.

### Dockerizing our Blog API

#### Overview
- we will go over the process of Dockerizing a Django app:
    - using a combination of Docker, Gunicorn for handling requests, and Nginx.
- We will also review the
    - `Dockerfile`
        - from this we can create an Image in different environments/systems
        - it describes the environment
            - that is helpful for other devs
    - `docker-compose.yml`
    - `nginx/default.conf`


#### 1. **Dockerfile**
- The `Dockerfile` defines the instructions to build the Docker image for the Django app. 
- It specifies the base image, dependencies, project files, and commands to be executed.

```Dockerfile
# Use a lightweight version of Python to minimize image size
FROM python:3.9-slim  

# Set the working directory inside the container
WORKDIR /usr/src/app  

# Systemabhängigkeiten installieren
RUN apt-get update
# Copy the requirements file into the working directory
COPY requirements.txt .  

# Upgrade pip and install Python dependencies
RUN pip install -r requirements.txt  

# Copy the entire project to the container
COPY . . 

# Collect static files for production
RUN python manage.py collectstatic --noinput  

RUN pip install gunicorn

# Open port 8000 for the application
EXPOSE 8000  

# Set the default command to run Gunicorn
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]

``` 
- Build command:
    - `docker build -t django_gunicorn .`

- to run our new Images:
    - `docker run -p 8080:8000 django_gunicorn:latest`
    - the container runs on port 8000 and is map to 8080
        - therefore we can access this docker web app via http://localhost:8080

#### **Nginx ** (`/nginx/default.conf`)
   - **Introduction**: The Nginx configuration file defines how Nginx will act as a reverse proxy, forwarding requests to the Django app running in the `web` container, while also serving static files.

```bash
# nginx/default.conf

server {
    listen 80;

    # Enable detailed error logging
    error_log /var/log/nginx/error.log debug;


    location / {
        proxy_pass http://web:8000;  # Gunicorn running in the `web` container
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /usr/src/app/staticfiles/;  # Path to your static files
    }
}
```

- **server { listen 80; }**: 
    - Listens on port 80 for incoming HTTP traffic.
- **location /static/ { alias /usr/src/app/static/; }**: 
    - Serves static files from the `static` folder inside the container.
- **location / { proxy_pass http://web:8000; }**: 
    - Forwards all other requests to the Gunicorn service running on port 8000 of the `web` container.
- **proxy_set_header**: 
    - Passes important headers like the original host and IP address to Gunicorn for proper handling.
    - scheme: HTTP or HTTPS
    - X-Forwarded-For: pass client IP address via many proxies

## Docker compose

- Now, you can use `docker compose` commands directly in the CLI.
- The Compose Specification defines multi-container microservices apps.  
- It's an open, community-led standard, separate from Docker’s code.
- This separation ensures better governance and clear responsibilities. 


### Compose files

- Compose uses YAML files to define microservices applications.

The default name for a Compose YAML file is `docker-compose.yaml`. However, it also accepts `docker-compose.yml`


