#! /bin/bash

# PURPOSE: this script is used to test that the DRF app inside the Docker container is actually responding
# Can be used in Travis build or on local developer machine

echo  Running test_proj.sh...

# Troubleshooting env var carry-forward - no longer exported, just declared in env.sh
echo DATABASE_PORT $DATABASE_PORT
echo MIKE_ENV_VAR $MIKE_ENV_VAR

#echo Trying to source the env.sh file...

#source ./budget_proj/bin/env.sh

echo Did the secret survive getting sourced by .travis.yml ?
echo DJANGO_SECRET_KEY-dummy $DJANGO_SECRET_KEY

#echo Setting key directly here to determine whether it is possible to ever pass the secret around as an env var...

#DJANGO_SECRET_KEY="m1o2gmv25hn0jny6xn3b3xo45zk70jw67dbef890mp1m012345"

#echo Reading secret key back that I just set directly here
#echo DJANGO_SECRET_KEY-dummy $DJANGO_SECRET_KEY

# Run all configured unit tests inside the Docker container
docker-compose -f budget_proj/docker-compose.yml run budget-service python manage.py test
