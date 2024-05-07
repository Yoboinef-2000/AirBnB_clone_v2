# This puppet manifest sets up the web servers for the deployment of web_static

exec { 'setUpWebServers':
  command  => "sudo apt-get -y update;
          sudo apt-get -y install nginx;
          sudo mkdir /data/;
          sudo mkdir /data/web_static/;
          sudo mkdir /data/web_static/releases/;
          sudo mkdir /data/web_static/shared/;
          sudo mkdir /data/web_static/releases/test/; 
          sudo echo 'Hello Fellow Papi Believers' | sudo tee /data/web_static/releases/test/index.html;

          sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;

          sudo chown -R ubuntu:ubuntu /data/;

          sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default;

          sudo service nginx restart",
  provider => shell,
}
