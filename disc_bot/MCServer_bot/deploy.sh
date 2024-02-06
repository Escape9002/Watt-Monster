#! /bin/bash
docker build -t mcserver .
docker run -d --env-file .env mcserver