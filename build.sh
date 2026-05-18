#!/usr/bin/env bash

# set shell settings (see https://sipb.mit.edu/doc/safe-shell/)
set -eu -o pipefail

HUGO_ARGS=""

# Change baseURL for branches other than master. Required to get relative
# links (like OpenGraph images) working on branches.
BRANCH_NAME="${GITHUB_REF:-}"
BRANCH_NAME="${BRANCH_NAME#refs/heads/}"
BRANCH_SLUG=$(echo $BRANCH_NAME | sed -e 's/[^A-Za-z0-9_-]/_/g')
if [[ -n "$BRANCH_SLUG" && "$BRANCH_SLUG" != "master" ]]; then
    BASE_URL="https://librepcb.org/_branches/$BRANCH_SLUG/"
    HUGO_ARGS+=" -b $BASE_URL"
    echo "Overriding baseURL for branch: $BASE_URL"
fi

# Run Hugo with Docker
docker run -t --rm -u `id -u`:`id -g` -v `pwd`:/work -w /work \
    librepcb/librepcb-dev:webtools-1 \
    hugo -F $HUGO_ARGS

# Make 404.html working on *any* path
sed -i 's/"\.\//"\//g' public/404.html
