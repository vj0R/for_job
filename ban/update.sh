#!/bin/bash

/usr/bin/ssh root@192.168.1.100 "sed -i -e 's/$1 0;//g' /etc/nginx/conf.d/ban && service nginx reload"

