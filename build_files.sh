#!/bin/bash

# Ensure Python is installed
export PATH=$HOME/.local/bin:$PATH

# Install dependencies
python3 -m ensurepip --default-pip
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput
