# Running FastAPI inside ShinyProxy

This repository describes how to add a FastAPI inside ShinyProxy (at least version 2.5.0).

# Build the Docker image

To pull the image made in this repository from Docker Hub, use

```
sudo docker pull openanalytics/shinyproxy-fastapi-demo
```

the relevant Docker Hub repository can be found at https://hub.docker.com/r/openanalytics/shinyproxy-fastapi-demo

To build the image from the Dockerfile, clone this repository, then navigate to its root directory and run

```
sudo docker build -t openanalytics/shinyproxy-fastapi-demo .
```

# ShinyProxy Configuration

To add the FastAPI to ShinyProxy, add the following lines to its configuration file (see [application.yml](./application.yml) for a complete file):
```
specs:
    - id: fastapi-demo
      display-name: FastAPI Demo Application
      container-image: openanalytics/shinyproxy-fastapi-demo
      target-path: "#{proxy.getRuntimeValue('SHINYPROXY_PUBLIC_PATH')}"
      port: 8080
      container-env:
        SCRIPT_NAME: "#{proxy.getRuntimeValue('SHINYPROXY_PUBLIC_PATH').replaceFirst('/$','')}"
```

# References
* https://fastapi.tiangolo.com/tutorial/
* https://kinsta.com/nl/blog/fastapi/


**(c) Copyright Open Analytics NV, 2024.**
