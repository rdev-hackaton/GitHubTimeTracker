#! /bin/bash

cat ${1} | grep clock | wc -l

exit 0