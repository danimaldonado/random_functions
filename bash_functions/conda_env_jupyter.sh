#!/bin/bash

echo Insert environment name

read envname

conda create --name $envname

source activate $envname

yes | conda install -c anaconda ipykernel 

yes | conda install -c conda-forge jupyterlab

python -m ipykernel install --user --name $envname --display-name "Python ($envname)"
