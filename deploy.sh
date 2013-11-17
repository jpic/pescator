#!/bin/bash
# This is how I avoid the need of fabric: with a 17 SLOC bash function.

# Runs a local function or remote command on one or several servers through ssh
# in given paths.
# For example, source this module and try:
##  # with a local function
##  function hello() { echo "Hello from `pwd`"; }
##  remote hello somehost: otherhost:/path/to/test
##  # with a remote command
##  remote "git pull origin master" somehost:/path
function remote() {
    local do="$1"
    shift
    local targets="$*"

    local target=""
    local target_host=""
    local target_path=""

    for target in $targets; do
        target_host="${target%%:*}"
        target_path="${target/$target_host:/}"

        if [[ -n "$(declare -f $do)" ]]; then
            echo "Running $do() on $target_host in $target_path"
            ssh $target_host "cd $target_path && $(declare -f $do) && $do"
        else
            echo "Running $do on $target_host in $target_path"
            ssh $target_host "cd $target_path && $do"
        fi
    done
}

git push origin master

function deploy() {
    source ../env/bin/activate
    git stash
    git pull origin master
    ./manage.py collectstatic -l --noinput
    ./manage.py migrate
    touch pescator/wsgi.py
}

remote deploy pescator@tina:pescator/
