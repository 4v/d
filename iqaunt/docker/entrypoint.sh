#!/bin/bash
set -e
sed -i "s|localhost|$MONGODB|" /home/jovyan/QUANTAXIS/QUANTAXIS/QAUtil/QASetting.py
exec "$@"

