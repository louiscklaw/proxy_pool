#!/usr/bin/env bash

set -ex

# docker rmi $(docker images -a -q)
docker builder prune -f
# docker image prune -f

docker build -t proxy_pool:latest .

docker-compose up
