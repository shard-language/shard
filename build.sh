#!/bin/bash

set -e

if ! dpkg -l | grep -q "ii  flex"; then
    echo "Flex is not installed."
    exit 1
fi

if ! dpkg -l | grep -q "ii  bison" ; then
    echo "Bison is not installed."
    exit 1
fi

if ! dpkg -l | grep -q "ii  gcc"; then
    echo "GCC is not installed."
    exit 1
fi

flex src/lexer.l
bison -d src/parser.y

gcc -o shard lex.yy.c parser.tab.c src/main.c -lfl