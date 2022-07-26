FROM alpine:3.16.0

RUN apk add transmission-daemon

COPY entrypoint.sh /entrypoint.sh
COPY settings.json /data/settings.json

CMD [ "/entrypoint.sh" ]
