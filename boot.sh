#!/usr/bin/env bash

echo "====================="
echo " 1401: FORMAL WHERE  "
echo "====================="

if ! hash node 2>/dev/null; then
    echo "Please install nodejs"
    exit 1
fi

# make pip requirements
pip install -r requirements.txt $@

# build react app
cd app/frontend; npm run build $@

# runserver
# cd app && python manpy runserver $@
cd ~/TheFormalWear/app && python manage.py runserver --settings=backend.prod_settings $@
