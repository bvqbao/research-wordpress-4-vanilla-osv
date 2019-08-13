from osv.modules import api

#api.require_running('mysql')
#api.require_running('php')

api.require('mysql')
api.require('php')

# REST APIs
api.require_running('httpserver')

default = api.run('/usr/bin/mysqld --defaults-file=/etc/my.cnf --datadir=/data --user=root --innodb-use-native-aio=0 &! /php/php-cgi -b 9000 -c /php/php.ini &! /lighttpd.so -D -f /lighttpd/lighttpd.conf')
