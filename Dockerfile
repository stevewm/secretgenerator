FROM python:3.13-rc-alpine3.20

WORKDIR /usr/src/app
EXPOSE 8000

COPY ./app .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "run", "./main.py"]
