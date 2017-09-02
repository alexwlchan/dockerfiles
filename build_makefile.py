#!/usr/bin/env python3.6
# -*- encoding: utf-8

import os
import subprocess

ROOT = subprocess.check_output(
    ['git', 'rev-parse', '--show-toplevel']).decode('ascii').strip()

dockerfiles = []

for item in os.listdir(ROOT):
    d = os.path.join(ROOT, item)
    if not os.path.isdir(d) or item.startswith('.'):
        continue

    if os.path.isfile(os.path.join(d, 'Dockerfile')):
        dockerfiles.append(item)

with open(os.path.join(ROOT, 'Makefile'), 'w') as f:
    for d in sorted(dockerfiles):
        f.write(f'{d}:\n\tdocker build --tag alexwlchan/{d} {d}\n\n')

    f.write(f'all: {" ".join(sorted(dockerfiles))}\n\n')
    f.write(f'.PHONY: all {" ".join(sorted(dockerfiles))}\n')
