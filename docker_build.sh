#!/usr/bin/env bash

set -ex

# docker rmi $(docker images -a -q)
docker container prune -f
# docker image prune -f

docker build -t proxy_pool:latest .

docker-compose build

docker container prune -f