#!/bin/bash

cd src

if [[ "${1}" == "celery" ]]; then
  echo "starting celery worker ..."
  celery --app=tasks.tasks:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
  echo "Starting flower..."
  celery --app=tasks.tasks:celery flower
 fi