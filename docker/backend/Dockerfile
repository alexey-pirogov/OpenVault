FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt -y update \
    && apt -y install gcc python3-dev musl-dev netcat-traditional curl

RUN apt-get -y update \
    && apt-get install linux-libc-dev

RUN apt-get -y update \
    && apt-get install -y libsm6 libxext6 libxrender-dev ffmpeg libgl1

RUN pip install --upgrade pip

WORKDIR /home/app/web

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

COPY . .

RUN python3 manage.py collectstatic --noinput

ENTRYPOINT ["sh", "./entrypoint.sh"]
