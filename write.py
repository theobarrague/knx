#!/usr/bin/env python

import sys

if len(sys.argv) < 4:
    print("Usage:", sys.argv[0], "ip", "group", "value")
    sys.exit(1)

from bof.layers.knx import group_write

group_write(sys.argv[1], sys.argv[2], sys.argv[3])
