from osv.modules import api

default = api.run('/php/php-cgi -b 9000 -c /php/php.ini -C')
