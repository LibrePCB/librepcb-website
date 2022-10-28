#!/bin/sh

# set shell settings (see https://sipb.mit.edu/doc/safe-shell/)
set -eu -o pipefail

FILES=`git diff --no-commit-id --name-only --diff-filter=AM master..HEAD -- *.gif`
for f in $FILES
do
  echo "$f"
  ./tools/process_image.sh "$f"
done
