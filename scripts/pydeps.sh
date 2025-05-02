#!/bin/zsh
# Path: /usr/local/bin/pydeps.sh
# Description: Run pydeps to generate a dependency graph of a python project

# Usage: pydeps.sh <path to python project>

# Check if pydeps is installed
if ! command -v pydeps &> /dev/null
then
    echo "pydeps could not be found"
    exit
fi

python3 -m pydeps ../src -T png -o dependencies.png --rmprefix src. --rankdir LR --cluster --keep-target-cluster --exclude-exact src.ui src.game src.utils
