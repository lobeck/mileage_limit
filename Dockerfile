FROM python:3-slim

ADD . /app
WORKDIR /app

RUN useradd -M --home-dir /app mileage

RUN pip --no-cache-dir --trusted-host pypi.org install --upgrade -r /app/requirements.txt pip libnacl \
  && pip install /app && rm -rf /app

USER mileage

ENTRYPOINT ["mileage"]
