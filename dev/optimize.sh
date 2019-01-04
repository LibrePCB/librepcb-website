#!/bin/bash

cd ./output

for f in *.png
do
  echo "$f"
  pngcrush -rem allb -brute -reduce -ow "$f"
done

for f in *.gif
do
  echo "$f"
  gifsicle --batch --colors 256 --optimize=3 "$f"
done
