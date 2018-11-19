#!/usr/bin/env sh

SAMPLEDIR="./sample"
PUBLICDIR="./public"

# Ensure that PUBLICDIR exists before extracting sample *.tar.gz files in it
mkdir -p $PUBLICDIR

echo "Bootsrapping web root directory with sample data"

for f in $SAMPLEDIR/*.tar.gz
do
  echo "Extracting sample file $f"
  tar -C $PUBLICDIR -xvzf $f
done

echo "Sample files extracted in the web root"
