sudo apt update
sudo apt install python3.5 -y
sudo apt install python3.5-dev -y
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient
sudo pip3 install pathlib

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE ask;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION;"
mysql -uroot -e "FLUSH   PRIVILEGES;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate