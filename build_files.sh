#!/bin/bash

# Create and activate a virtual environment in Vercel's environment
 # On Windows, use venv\Scripts\activate

# Upgrade pip inside the virtual environment
pip install --upgrade pip

# Install dependencies inside the virtual environment
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

