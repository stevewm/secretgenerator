FROM python:3.12.3-slim-bullseye

WORKDIR /usr/src/app
EXPOSE 8000

COPY ./app .
COPY requirements.txt .

RUN pip install --upgrade pip \
    pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "run", "./main.py"]
