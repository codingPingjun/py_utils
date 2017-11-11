#!/usr/bin/env bash

cd ../
echo "Enter into project directory..."
rm -rf dist pydaily.egg-info
python setup.py sdist upload -r pypi
rm -rf build
python setup.py sdist bdist_wheel

# twine upload -r test --sign dist/pydaily-
