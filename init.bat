cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
goto start
mysql -u root -p
mysql -uroot -e "CREATE DATABASE ask;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION;"
mysql -uroot -e "GRANT RELOAD ON *.* TO 'box'@'localhost';"
mysql -uroot -e "FLUSH   PRIVILEGES;"
:start
python C:/home/box/web/ask/manage.py migrate
python C:/home/box/web/ask/manage.py runserver