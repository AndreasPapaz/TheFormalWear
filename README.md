```
                     /$$ /$$   /$$  /$$$$$$    /$$  
                   /$$$$| $$  | $$ /$$$_  $$ /$$$$  
                  |_  $$| $$  | $$| $$$$\ $$|_  $$  
                    | $$| $$$$$$$$| $$ $$ $$  | $$  
                    | $$|_____  $$| $$\ $$$$  | $$  
                    | $$      | $$| $$ \ $$$  | $$  
                   /$$$$$$    | $$|  $$$$$$/ /$$$$$$
                  |______/    |__/ \______/ |______/
```
---
for reference: https://www.djangoproject.com
# to get started...

```sh
$ cd TheFormalWear
$ easy_install pip (if you do not have pip)
$ pip install virtualenv
$ pip install virtualenvwrapper
```

## after you get virtualenvwrapper make sure you edit your `/.bashrc` or what ever profile you have

i.e.)
```sh
$ vim ~/.bashrc
```

## add the following to this file ^^^

```python
export PIP_REQUIRE_VIRTUALENV=false
# virtualenv wrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

## now create a virtual env `mkvirtualenv -p python3 "app_name"`
use `workon` to create a new virtual env and name it what ever you want

then......
```sh
$ ./boot.sh
```
