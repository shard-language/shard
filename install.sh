#!/bin/bash

# Please notice that this program must be run as root

set -e

if [ ! "$(id -u)" -eq 0]; then
    echo "This program requires root permissions."
    exit 1
fi

if [ ! -f "sharp" ]; then
    echo "Could not find Sharp."
    exit 1
fi

mv sharp /usr/bin/sharp