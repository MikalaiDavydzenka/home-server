#!/bin/sh

set -x

exec transmission-daemon \
    --bind-address-ipv4 "${BIND_IPV4:-0.0.0.0}" \
    --bind-address-ipv6 "${BIND_IPV6:-::}" \
    --port "${PORT:-9091}" \
    --watch-dir "${WATCH_DIR:-/data/watch}" \
    --incomplete-dir "${INCOMPLETE_DIR:-/data/incomplete}" \
    --download-dir "${DOWNLOAD_DIR:-/data/download}" \
    --config-dir "${CONFIG_DIR:-/data}" \
    --peerport "${PEER_PORT:-51413}" \
    --auth \
    --username "${USER_NAME:-torrent}" \
    --password "${PASSWORD:-torrent}" \
    --foreground
