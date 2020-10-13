#!/bin/bash
# Based on Taskfile (https://github.com/adriancooney/Taskfile)
set -o errexit  # quit on error
set -o nounset  # undefined is error
set -o pipefail # show last commmand in pipe to crash

function help {
    echo "$0 <task> <args>"
    echo "Tasks:"
    compgen -A function | cat -n
}

function debug {
    SKELETON_LOG_LEVEL='DEBUG'
    export SKELETON_LOG_LEVEL
    serve
}

function serve {
    cd skeleton/
    python manage.py runserver
}

function test {
    # display all warnings
    python -Walways skeleton/manage.py test core.tests
}

TIMEFORMAT="Task completed in %3lR"
time "${@:-help}"
