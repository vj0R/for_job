#!/usr/bin/python3

import os
import pymysql

try:
    os.remove('/tmp/optimize.sql')
except:
    print('file not delete')

conn = pymysql.connect(host='ip', user='root', passwd='pass')
cur = conn.cursor()
cur.execute('''SELECT concat("OPTIMIZE TABLE ", table_schema,".",table_name,";")
FROM information_schema.tables WHERE DATA_FREE > 0 INTO OUTFILE \'/tmp/optimize.sql\';''')
conn.commit()


with open('/tmp/optimize.sql') as file:
    for line in file.readlines():
        cur.execute(line)
        conn.commit()
        print(line, '--> [Ok]')

