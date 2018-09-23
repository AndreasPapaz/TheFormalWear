#!/usr/bin/env bash

echo "====================="
echo "1401: THE FORMAL WEAR"
echo "====================="

if ! hash node 2>/dev/null; then
    echo "Please install nodejs"
    exit 1
fi

# make pip requirements
pip install -r requirements.txt $@

# runserver
cd the_formal_wear && python manage.py runserver $@
