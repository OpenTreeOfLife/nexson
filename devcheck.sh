#!/bin/bash
echo 'running tests, then prospector (several python checking prereqs must be installed), and sphinx.'
set -x
python setup.py test || exit
prospector nexson || exit
cd doc || exit 
make html || exit
cd -
