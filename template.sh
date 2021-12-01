#!/bin/bash

#Takes argument of the day number for the problem
# usage ./template.sh 3

mkdir "d${1}"
cp template.py "d${1}/p1.py"
touch "d${1}/input.txt"
touch "d${1}/test.txt"
