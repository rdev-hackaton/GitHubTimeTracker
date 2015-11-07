#! /bin/bash

VALID="$(cat ${1} | grep ':clock' | wc -l)"
if [[ $VALID -eq 0 ]]; then
    echo "You have to include time in commit message, eg. \":clock1: 5m | rest_of_message\" !"
    echo "Aborting..."
    exit 1
fi
exit 0

