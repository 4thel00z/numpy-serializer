#! /usr/bin/zsh

version=$(pipenv run python3 -c "import numpy_serializer;print(numpy_serializer.__version__)")
python3 -m twine upload dist/numpy*$version*
