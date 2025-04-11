#!/bin/bash

set -e

if [ "$EUID" -ne 0 ]; then
    echo "[ ERR ] The Shard installation program must be executed as root"
    exit 1
fi

echo "The Shard programming language compiler -- Installation program"

echo "Looking for Python3..."
if ! command -v python3 &>/dev/null; then
    echo "[ WARN ] Python3 not found on your system. Install it? (y/n) "
    read answer
    if [ "$answer" == "y" ]; then
        apt install python3
    else
        echo "[ ERR ] Missing required dependencies"
        exit 1
    fi
fi

echo "Looking for pip..."
if ! command -v pip &>/dev/null; then
    echo "[ WARN ] pip not found on your system. Install it? (y/n) "
    read answer
    if [ "$answer" == "y" ]; then
        apt install python3-pip
    else
        echo "[ ERR ] Missing required dependencies"
        exit 1
    fi
fi

echo "Looking for PLY..."
if ! pip show ply &>/dev/null; then
    echo "[ WARN ] PLY not found on your system. Install it? (y/n) "
    read answer
    if [ "$answer" == "y" ]; then
        pip install ply
    else
        echo "[ ERR ] Missing required dependencies"
        exit 1
    fi
fi

echo "Looking for PyInstaller..."
if ! pip show pyinstaller &>/dev/null; then
    echo "[ WARN ] PyInstaller not found on your system. Install it? (y/n) "
    read answer
    if [ "$answer" == "y" ]; then
        pip install pyinstaller
    else
        echo "[ ERR ] Missing required dependencies"
        exit 1
    fi
fi

echo "Creating executable..."
pyinstaller --onefile src/shard.py

echo "Cleaning..."
rm -r build
mv dist/shard src/shard
rm -r dist
rm shard.spec

echo "Creating command..."
mv src/shard /usr/bin/shard

echo "Installation complete!"
echo "Type 'shard --version' to see if the language is correctly installed"