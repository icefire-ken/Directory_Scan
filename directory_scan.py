#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

spedir = 'E:\Downloads'

for curdir, dirs, files in os.walk(spedir):
    print(f'\n=== {curdir} ===\n')
    print(dirs)
    for file in files:
        print(os.path.join(curdir, file))

