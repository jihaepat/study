#!/usr/bin/env bash

# pyenv 설치

# study 프로젝트 세팅
pyenv virtualenv 3.6.4 study
pyenv local study
pip install -U -r dev-requirements.txt

