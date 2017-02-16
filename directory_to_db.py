#!/usr/bin/python3

import subprocess as sub
import pymysql
conn = pymysql.connect(host='192.168.1.1', user='python', passwd='pass', db='python', charset='utf8')

path1 = input()
command1 = 'ls -la ' + str(path1)
com = sub.Popen(command1,  shell=True, stdout=sub.PIPE)
result = com.stdout.read()
ll = [i for i in result.decode('utf8').split('\n')]
rl = ll[3:]
cur = conn.cursor()
cur.execute("DELETE FROM `list`")
conn.commit()
for i in range(0,len(rl)-1):

    mylist = list(filter(None, rl[i].split(' ')))
    dat = mylist[5] + ' ' + mylist[6] + ' ' + mylist[7]
    zapr = r"INSERT INTO `list` (`chmod`, `p2`, `p3`, `p4`, `p5`, `data`, `file`) VALUES ('{}', {}, '{}', '{}', {}, '{}', '{}')".format(mylist[0], mylist[1], mylist[2], mylist[3], mylist[4], dat, mylist[8])
    cur.execute(zapr)
conn.commit()
cur.close()
conn.close()



