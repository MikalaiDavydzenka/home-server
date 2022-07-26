FROM alpine:3.16.0

RUN apk add samba

COPY entrypoint.sh /entrypoint.sh
COPY smb.conf /etc/samba/smb.conf

CMD [ "/entrypoint.sh" ]
