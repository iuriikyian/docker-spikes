#!/bin/bash

cd ..

IMAGE_NAME=docker-enty-test
PORT=8001

# source config/_env/elastic-secret.env

PS3='Please enter your choice: '
options=("build" "run-server" "run-batch" "run-shell" "quit")
select opt in "${options[@]}"
do
    case $opt in
        "build")
            docker build -t ${IMAGE_NAME} -f server/docker/dockerfile .
            break
            ;;
        "run-server")
            docker run --rm -i -t \
                --env-file=server/config/server.config.env \
                -p ${PORT}:${PORT} ${IMAGE_NAME}
            break
            ;;
        "run-batch")
            docker run --rm -i -t \
                --env-file=server/config/batch.config.env \
                ${IMAGE_NAME} batch
            break
            ;;
        "run-shell")
            docker run --rm -i -t \
                ${IMAGE_NAME} /bin/bash
            break
            ;;
        "quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

cd -