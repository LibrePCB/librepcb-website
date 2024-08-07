#!/bin/sh

# set shell settings (see https://sipb.mit.edu/doc/safe-shell/)
set -eu -o pipefail

python3 tools/add_progressbar_to_gif.py $@

gifsicle --optimize=3 --colors 256 --lossy -j8 -o $@ $@
