#!/bin/bash

cur_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/
PROTOC_DIR=${cur_dir}../protoc/
PYTON_DIR=${cur_dir}../client/
JAVA_DIR=${cur_dir}../server/src/main/java/

for po in $PROTOC_DIR/*; do
    echo $po
    protoc -I$PROTOC_DIR --python_out="${PYTON_DIR}" $po
done

for po in $PROTOC_DIR/*; do
    echo $po
    protoc -I$PROTOC_DIR --java_out="${JAVA_DIR}" $po
done

echo ""
echo "ALL DONE!"
