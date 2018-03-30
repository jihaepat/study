#!/usr/bin/env bash

# pyenv 설치

# jtelips 프로젝트 세팅
pyenv virtualenv 3.6.4 TDD
pyenv local TDD
pip install -U -r requirements.txt


