#!/usr/bin/env bash

SAMPLEDIR="./sample"
PUBLICDIR="./public"

echo "Bootsrapping web root directory with sample data"

for f in $SAMPLEDIR/*.tar.gz
do
  echo "Extracting sample file $f"
  tar xvzf -C $PUBLICDIR $f
done

echo "Sample files extracted in the web root"
