#!/bin/bash

CONTROL_FILE="DEB/DEBIAN/control"

DEBPKG="timetest-0.01.deb"

echo "Making timetest release... "

rm -fv *.deb
rm -vf -r `find DEB/opt/timetest/*`

echo -n "Copyng scripts... "
cp -u app.py DEB/opt/timetest/ || exit 0
echo "done"

echo -n "Copyng pyc... "
cp -r -u __pycache__ DEB/opt/timetest/ || exit 0
echo "done"

echo -n "Coping YaML.. "
cp -r -u openapi-3 DEB/opt/timetest/ || exit 0
echo "done"

date +%F >DEB/opt/timetest/.build
dpkg -b DEB $DEBPKG || exit 1
echo "$DEBPKG is ready."
