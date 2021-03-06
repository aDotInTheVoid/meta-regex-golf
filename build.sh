#!/usr/bin/env bash

# Each folder has different cargo configs, so we can't use a workspace

mkdir -p out
for i in v*
do
    cd $i
    cargo build --release
    cp target/release/$i ../out
    cd ..
done
