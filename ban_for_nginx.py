#!/usr/bin/python3

import re
import os

IP = "192.168.1.100" # NGINX SERVER
file=open("/var/log/iptables.log")
sp=re.findall('[\d]+\.[\d]+\.[\d]+\.[\d]+', file.read())

ll=set(sp)
for i in ll:
    s1=sp.count(i)
    if (s1>20 and i!=IP):
        comm="echo '"+ str(i) +" 0;' >> /etc/nginx/conf.d/ban"
        os.system(comm)

os.system("/usr/sbin/service nginx reload")
file.close()

