#!/bin/sh

echo 'generator.c' | entr -c -s 'gcc generator.c -o generator && ./generator'
