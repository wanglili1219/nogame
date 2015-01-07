#!/bin/bash

cur_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/
PROJ_DIR=${cur_dir}../server/src/main/java/com/ease/nogame/dict/
PROJ_DICT_DIR=${cur_dir}../server/src/main/resources/dict/
JAVA_DIR=${cur_dir}java/
DICT_DIR=${cur_dir}../dict/
TMPL_LIST=(dict_javabean.tmpl dict_beanmgr.tmpl)

which cheetah > /dev/null
if [ $? != 0 ]; then
    echo "ERROR: not found cheetah, please install it."
    exit 1
fi

for t in ${TMPL_LIST[@]};
do
    if [ ! -e ${cur_dir}$t ]; then
        echo "ERROR: not found "${cur_dir}$t
        continue
    fi

    cheetah compile ${cur_dir}$t
done

rm -rf ${JAVA_DIR}*
${cur_dir}gen_javabean.py
[ $? != 0 ] && (echo "ERROR: generate java class";exit 1)
rm -rf ${PROJ_DIR}*
cp -Rvp ${JAVA_DIR}* $PROJ_DIR

if [ ! -e ${PROJ_DICT_DIR} ]; then
    mkdir -p ${PROJ_DICT_DIR}
fi

rm -rf ${PROJ_DICT_DIR}*
cp -Rvp ${DICT_DIR}* $PROJ_DICT_DIR

echo ""
echo "ALL DONE!"

