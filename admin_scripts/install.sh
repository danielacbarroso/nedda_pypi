#!/bin/bash
apt-get update
apt-get install -y nginx python-pip build-essential python-dev libmysqlclient-dev
cd /etc/nginx/sites-enabled
ln -s /opt/nedda/web_service/web_service/nginx_configuration_uwsgi nedda_configuration
pip install -r /opt/nedda/admin_scripts/requirements
cd /opt/nedda/web_service
cp config_exemplo config
chown gat:gat config
sudo mkdir -p /var/log/uwsgi
