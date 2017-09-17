# news-recommendation

## About

This is a web app that:
- Built with React.
- Collect news from multiple news sources and apply ML: tf-idf to remove duplicates all & tensorflow CNN to predict news topic,
- Service Oriented, multiple backend servces commucating through jsonrpc, 
- Automatically recommend news based on user click logs. 

Click here to see the [demo](http://34.214.18.41:3000/)
- You can either sign up or use my account yangyang729@gmail.com / 12345678 to login.
- Because the demo runs on Amazon free tier instance, it is not fully functioning in terms of model traning and news recommendation.

## To-Do:

- Sorted by recommendation score.
- Refactor Login system using Autho0
- Text cleaning, model tuning
- ...


## Setup
install redis
```
sudo apt install make
sudo apt-get update
sudo apt-get install gcc

wget http://download.redis.io/releases/redis-3.2.6.tar.gz
tar xzf redis-3.2.6.tar.gz
cd redis-3.2.6
make
sudo make install
cd utils
sudo ./install_server.sh

sudo service redis_6379 start
```

install python
```
sudo apt-get install python
sudo apt-get install python-pip
```
install node.js
```
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install -y nodejs
```
install mongodb
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org

sudo service mongod start
```




## PyLint
specify which python version to use
```
python2 -m pylint cloudAMQP_client.py
```

To modify a file in place (with aggressive level 2):

```
autopep8 --in-place --aggressive --aggressive <filename>
```
