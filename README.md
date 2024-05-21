# Running FastAPI apps inside ShinyProxy

In order to run FastAPI apps using ShinyProxy you have to consider two things:

- use a [web server](https://fastapi.tiangolo.com/deployment/manually/) to run
  the app.
- ensure to use the `url_for` helper when referencing other pages and static
  files. The HTML files in the [app/templates](app/templates) directory show the
  proper usage of the `url_for` helper. For example:

    ```html
    <link rel="stylesheet" href="{{ url_for('static', path='style.css') }}">
    <a href="{{ url_for('about') }}">About</a>
    <img width="400px" src="{{ url_for('static', path='logo.png') }}">
    <script src="{{ url_for('static', path='script.js') }}"></script>
    ```


# Build the Docker image

To pull the image made in this repository from Docker Hub, use

```bash
sudo docker pull openanalytics/shinyproxy-fastapi-demo
```

the relevant Docker Hub repository can be found at <https://hub.docker.com/r/openanalytics/shinyproxy-fastapi-demo>.

To build the image from the Dockerfile, clone this repository, then navigate to its root directory and run

```bash
sudo docker build -t openanalytics/shinyproxy-fastapi-demo .
```

# ShinyProxy Configuration

To add the FastAPI app to ShinyProxy, add the following lines to its
configuration file (see [application.yml](./application.yml) for a complete
file):

```yaml
proxy:
  specs:
    - id: fastapi-demo
      display-name: FastAPI Demo Application
      container-image: openanalytics/shinyproxy-fastapi-demo
      port: 8000
      target-path: "#{proxy.getRuntimeValue('SHINYPROXY_PUBLIC_PATH')}"
      container-env:
        SCRIPT_NAME: "#{proxy.getRuntimeValue('SHINYPROXY_PUBLIC_PATH').replaceFirst('/$','')}"
```

Note that the `SCRIPT_NAME` environment variable may not end with `/`, therefore
we have to strip it from the variable.

## References

- <https://fastapi.tiangolo.com/tutorial/>
- <https://kinsta.com/nl/blog/fastapi/>
- [Running Flask app in ShinyProxy](https://github.com/openanalytics/shinyproxy-flask-demo)
- [ShinyProxy.io](https://shinyproxy.io/)
- [All demos](https://shinyproxy.io/documentation/demos/)

**(c) Copyright Open Analytics NV, 2024.**
