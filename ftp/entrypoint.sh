#!/bin/sh

set -x

FTP_USER="localftp"
FTP_PASSWORD="password"

FTP_GROUP=${FTP_USER}
FTP_FOLDER="/data"

echo -e "$FTP_PASSWORD\n$FTP_PASSWORD" | adduser -h ${FTP_FOLDER} ${FTP_USER}
mkdir -p ${FTP_FOLDER}
chown ${FTP_USER}:${FTP_GROUP} ${FTP_FOLDER}


MIN_PORT=${MIN_PORT:-21000}
MAX_PORT=${MAX_PORT:-21010}

vsftpd -opasv_min_port=$MIN_PORT -opasv_max_port=$MAX_PORT /etc/vsftpd.conf
[ -d /var/run/vsftpd ] || mkdir /var/run/vsftpd
pgrep vsftpd | tail -n 1 > /var/run/vsftpd/vsftpd.pid
exec pidproxy /var/run/vsftpd/vsftpd.pid true
