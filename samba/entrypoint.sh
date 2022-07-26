#!/bin/sh

set -x

exec smbd \
    --debug-stdout \
    --no-process-group \
    --foreground
