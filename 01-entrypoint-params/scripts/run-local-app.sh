#!/bin/bash

cd ..

source config/server.config.env

export SHOW_OPENAPI=true
export PORT
export PATH_PREFIX

cp VERSION server/VERSION
cd server

uvicorn app.main:app --port $PORT --reload