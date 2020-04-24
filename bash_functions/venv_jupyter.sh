#!/bin/bash

echo Insert environment name

read envname

echo Insert the full path where .env will live

read envpath

python -m venv $envpath/.env

source $envpath/.env/bin/activate

pip install --upgrade pip

pip install jupyter

python -m ipykernel install --user --name $envname --display-name "Python ($envname)"
