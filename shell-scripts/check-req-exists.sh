#!/bin/bash
FILE=./requirements.txt

if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "creating $FILE."
    touch $FILE
    echo "created $FILE."
fi