#!/bin/bash

TASK
if [[ $# == 0 ]]
then
    echo run without params
    export TASK=SERVER
else
    if [[ $# == 1 ]] && [[ $1 == "batch" ]]
    then
        echo run with one param: $1
        export TASK=BATCH
    else
        echo not expected count of params: $#
        exit 1
    fi
fi

. /opt/conda/etc/profile.d/conda.sh
. /opt/conda/bin/activate server

if [[ $TASK == "SERVER" ]]
then
    uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
else
    python /app/server/batch/run-batch.py
fi