#!/bin/bash
echo "loggin into to external shit"
FILE=/home/pi/Desktop/Final/Final.db
FILE2=/home/pi/Desktop/Final/test.csv
sshpass -p 'JesusIsGrounded123' sftp -oBatchMode=no -b- -oStrictHostKeyChecking=no root@198.199.77.252 <<_EOF_
cd /var/www/Flask/Flask
put $FILE
put $FILE2
bye
_EOF_

echo "peacin out"
exit 0
