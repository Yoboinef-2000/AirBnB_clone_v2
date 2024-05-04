#!/usr/bin/env bash
# This script sets up my webservers for the deployment of web_static

sudo apt-get -y update
sudo apt-get install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/ 
sudo mkdir /data/web_static/releases/test/ 
sudo echo "Hello Fellow Papi Believers" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

theConfig="/etc/nginx/sites-available/default"
sudo sed -i '/hbnb_static/ {s/^/#/}' $theConfig
sudo sed -i 's/^\tlocation \/ {/&\n\t\tlocation \/hbnb_static\/ {\n\t\t\talias \/data\/web_static\/current\/;\n\t\t}\n/' $theConfig

sudo service nginx restart
