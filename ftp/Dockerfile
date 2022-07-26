FROM alpine:3.16.0

RUN apk add vsftpd

COPY entrypoint.sh /entrypoint.sh
COPY vsftpd.conf /etc/vsftpd.conf

CMD [ "/entrypoint.sh" ]
