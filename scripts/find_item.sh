#!/bin/bash

# Find word within directory of files
# ./find_item.sh <keyword>

# Word to search for
key=$1

for f in $(ls);
do
    # if word found in file, print filename with filtered output
    cat $f | grep $key && echo $f
done
