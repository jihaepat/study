#!/usr/bin/env bash

pyenv virtualenv 3.6.4 study
pyenv local study

#fasttext 다운
git clone https://github.com/jihaepat/fastText.git

# word-embeddings-benchmarks 다운
git clone https://github.com/jihaepat/word-embeddings-benchmarks.git

cd fastText
pip install -U -r fastText/.
cd ..
cd word-embeddings-benchmarks
pip install -U -r word-embeddings-benchmarks/requirements.txt