#!/usr/bin/bash

for file in *; do
	echo "adding $file"
	git add $file
	git commit -m $file
done
