#!/bin/bash
until python main.py; do
    echo "'main.py' crashed with exit code $?. Restarting." >&2
    sleep 1
done
