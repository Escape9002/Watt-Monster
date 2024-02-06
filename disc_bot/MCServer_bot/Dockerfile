FROM python:3

FROM gorialis/discord.py

ADD ./requirements.txt ./
RUN pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt

RUN apt-get update && apt-get install -y iputils-ping

RUN mkdir -p /usr/src/dnd-historian

WORKDIR /usr/src/dnd-historian

COPY . . 

CMD ["python3", "DnDHistorian.py"]