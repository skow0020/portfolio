#!/bin/sh

# pylint
poetry run python -m pylint
if [ $? -ne 0 ]; then
 echo “pylint failed”
 exit 1
fi
