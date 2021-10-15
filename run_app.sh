#!/usr/bin/bash
set -e

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${DIR}/


# Launch the app
gunicorn -w 2 \
         --threads 1 \
         -b 0.0.0.0:8080 \
         --preload \
         --log-level debug \
         --access-logfile - \
         --error-logfile - \
         app.wsgi:app
