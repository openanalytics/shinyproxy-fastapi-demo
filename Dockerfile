FROM python:3.10

RUN apt-get update

WORKDIR /code

COPY ./app /code/.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3838

CMD ["uvicorn", "main:app", "--proxy-headers", "--forwarded-allow-ips", "*", "--host", "0.0.0.0", "--port", "3838"]

