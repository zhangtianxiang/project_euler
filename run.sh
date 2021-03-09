#!/bin/bash
set -e
if [ 1 != $# ]; then
    echo "usage: sh run.sh 1"
    exit
fi
echo "Run Solution.Solution$1"
go run . "Solution$1"
