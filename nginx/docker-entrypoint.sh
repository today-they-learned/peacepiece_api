#!/bin/bash

# Wait for Gunicorn
chmod +x /wait-for-it.sh
/wait-for-it.sh webapp:8888 --timeout=0 -- nginx -g 'daemon off;'
