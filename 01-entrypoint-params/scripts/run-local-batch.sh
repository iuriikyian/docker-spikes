#!/bin/bash

cd ..

source config/batch.config.env

export BATCH_PARAM

cd server

python batch/run-batch.py