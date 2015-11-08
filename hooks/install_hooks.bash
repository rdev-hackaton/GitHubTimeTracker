#!/usr/bin/env bash

CURRDIR=${0%/*}
BASEDIR=$(git rev-parse --show-toplevel)

ln -s -f ../../hooks/commit-msg.py ${BASEDIR}/.git/hooks/commit-msg
echo "Hooks installed"
