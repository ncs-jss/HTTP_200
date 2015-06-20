pip install django
pip install django_couchbase
sudo apt-get install coinor-cbc
sudo apt-get install python-dev
sudo wget -O/etc/apt/sources.list.d/couchbase.list http://packages.couchbase.com/ubuntu/couchbase-ubuntu1204.list
wget -O- http://packages.couchbase.com/ubuntu/couchbase.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install libcouchbase2-libevent libcouchbase-dev
#http://stackoverflow.com/questions/27670497/ubuntu-trying-to-install-python-couchbase-lib-libcouchbase-couchbase-h-no
pip install couchbase
