#!/bin/bash

source ./env/bin/activate

python src/logistic_regression.py
python src/neural_network.py
python src/vectorizer.py

deactivate