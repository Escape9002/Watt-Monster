FROM python:3

FROM gorialis/discord.py

ADD ./requirements.txt ./
ADD .ssh/ssh_key.pub root/.ssh/id_rsa.pub
ADD .ssh/ssh_key /root/.ssh/id_rsa 

RUN pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

RUN apt-get update && apt-get install -y iputils-ping

RUN mkdir -p /usr/src/mc-server

WORKDIR /usr/src/mc-server

COPY . . 

CMD ["python3", "MCServer.py"]
