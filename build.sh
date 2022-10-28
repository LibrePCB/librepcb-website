#!/usr/bin/env bash

# set shell settings (see https://sipb.mit.edu/doc/safe-shell/)
set -eu -o pipefail

# Run Hugo with Docker
docker run -t --rm -u `id -u`:`id -g` -v `pwd`:/work -w /work \
    librepcb/librepcb-dev:webtools-1 \
    hugo -F

# Make 404.html working on *any* path
sed -i 's/"\.\//"\//g' public/404.html
