#!/bin/bash

# Author : thewhiteh4t

# This script will automatically setup a vulnerable docker container for GitLab v12.8.1-ce

if [[ $(id -u) -ne 0 ]] ; then echo "Please run as root" ; exit 1 ; fi

echo "[+] Creating directory for volume..."
mkdir -p /srv/gitlab

echo "[+] Setting GITLAB_HOME..."
export GITLAB_HOME=/srv/gitlab

echo "[+] Starting GitLab..."
docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 22:22 \
  --name gitlab \
  --restart always \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  gitlab/gitlab-ce:12.8.1-ce.0

# Check build logs in separate terminal -> docker logs -f gitlab

echo
echo "[*] Logs  -> docker logs -f gitlab"
echo "[*] Shell -> docker exec -it gitlab /bin/bash"
