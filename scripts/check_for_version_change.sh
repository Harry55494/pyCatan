#!/bin/bash

git diff --name-only | if ! grep --quiet "src/version.py"
then
    echo "Version file has not been updated. Please update src/version.py."
    exit 1
fi
