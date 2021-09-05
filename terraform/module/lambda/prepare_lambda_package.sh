# bin/bash

# Usage: prepare_lambda_package.sh [path.module]
#
# prepare_lambda_package.sh prepares a python package which include third party package.
# Directory structure of terraform module must be
#   some_module
#   ├── src
#   │   └─ your python files here
#   ├── upload
#   │   ├── prepare     <- will be auto generated
#   │   └── lambda.zip  <- will be auto generated
#   └── prepare_lambda_package.sh
#   └── your tf files here

# Identity absolute path of module
if [ "$1" = "" ]; then
    echo "ERROR: you must specify module path"
    exit 1
fi
MODULE_RELATIVE_PATH=$1

dirname="$(cd -- "$(dirname -- "$MODULE_RELATIVE_PATH")" && pwd)" || exit $?
MODULE_ABSOLUTE_PATH="${dirname%/}/$(basename -- "$MODULE_RELATIVE_PATH")"

# Prepare a python package
rm -rf "$MODULE_ABSOLUTE_PATH"/upload/prepare
mkdir -p "$MODULE_ABSOLUTE_PATH"/upload/prepare
cp -r "$MODULE_ABSOLUTE_PATH"/src/* "$MODULE_ABSOLUTE_PATH"/upload/prepare/

cd "$MODULE_ABSOLUTE_PATH"/upload/prepare
pipenv lock -r > "$MODULE_ABSOLUTE_PATH"/upload/prepare/requirements_vendor.txt
pip install -r "$MODULE_ABSOLUTE_PATH"/upload/prepare/requirements_vendor.txt --no-deps -t "$MODULE_ABSOLUTE_PATH"/upload/prepare
rm "$MODULE_ABSOLUTE_PATH"/upload/prepare/requirements_vendor.txt
