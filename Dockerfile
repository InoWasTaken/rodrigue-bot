FROM python:3.9-alpine

WORKDIR /app
RUN apk add gcc musl-dev
RUN pip3 install --user discord.py

COPY villagers.json bot.py ./

ENTRYPOINT python3 bot.py