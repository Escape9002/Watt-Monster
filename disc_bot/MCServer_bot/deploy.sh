#! /bin/bash
# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <parameter>"
    exit 1
fi

# Assign input parameter to a variable
param=$1

docker build -t mcserver .

# Check the value of the input parameter and execute the corresponding code snippet
if [ "$param" = "debug" ]; then
    docker run --env-file .env mcserver    
else
    docker run -d --env-file .env mcserver
fi