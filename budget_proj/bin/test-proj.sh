#! /bin/bash

# PURPOSE: this script is used to test that the DRF app inside the Docker container is actually responding
# Can be used in Travis build or on local developer machine

echo  Running test_proj.sh...

# Troubleshooting env var carry-forward - former set with export, latter set with setenv
echo DATABASE_PORT $DATABASE_PORT
echo MIKE_ENV_VAR $MIKE_ENV_VAR

# Run all configured unit tests inside the Docker container
docker-compose -f budget_proj/docker-compose.yml run budget-service python manage.py test
