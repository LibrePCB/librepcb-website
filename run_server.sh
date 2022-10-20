#!/usr/bin/env bash

# set shell settings (see https://sipb.mit.edu/doc/safe-shell/)
set -eu -o pipefail

# Run Hugo with Docker
docker run -t --rm -u `id -u`:`id -g` -v `pwd`:/work -w /work -p 1313:1313 \
    librepcb/librepcb-dev:webtools-1 \
    hugo server -F --bind 0.0.0.0
