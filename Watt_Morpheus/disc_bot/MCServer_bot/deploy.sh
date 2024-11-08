#! /bin/bash
# Assign input parameter to a variable
param=$1

docker build -t mcserver .

# Check the value of the input parameter and execute the corresponding code snippet
if [ "$param" = "debug" ]; then
    docker run --env-file .env --network host --name mcserver -u mcserver    
else
    docker run -d --env-file .env --network host --restart unless-stopped --name mcserver mcserver
fi
