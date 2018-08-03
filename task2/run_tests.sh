#!/bin/sh

PYTHONPATH=brackets python -m pytest --cov-report html --cov-report term  --cov-branch --cov=brackets tests