#!/usr/bin/env bash
echo "Removing old dist"
rm -rf dist

echo "Generating dist"
python3 setup.py bdist_wheel --universal

echo "done"
