#!/bin/sh

# pylint
poetry run python -m pytest
if [ $? -ne 0 ]; then
 echo “pylint failed”
 exit 1
fi
