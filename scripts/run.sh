#!/bin/sh
set -e
gunicorn -b :8080 django_plotly.wsgi:application
