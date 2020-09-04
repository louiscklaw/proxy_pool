#!/usr/bin/env bash

set -ex

# prepare python
apt-get update
apt-get install -y python3 python3-pip



# start yml
apt-get update

apt-get install -y apt-transport-https
apt-get install -y ca-certificates
apt-get install -y curl
apt-get install -y software-properties-common

# install docker start
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"

apt-get update
apt-get install -y docker-ce

mkdir -p /etc/docker

# pip install -r requirements.txt
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose --version

python3 -m pip install -r requirements.txt

python3 test.py

./docker_build.sh
