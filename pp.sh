#!/bin/bash
var = pwd
cd var
git add *
git commit -m "fake commit"
git push origin master
echo "Commited sucessfully:-)"