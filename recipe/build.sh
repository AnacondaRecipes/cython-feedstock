#!/usr/bin/env bash

export CFLAGS="-I${PREFIX}/include -L${PREFIX}/lib ${CFLAGS}"
${PYTHON} setup.py install --single-version-externally-managed --record=record.txt
