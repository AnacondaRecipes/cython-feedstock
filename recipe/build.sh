#!/usr/bin/env bash

if [[ ${HOST} =~ .*darwin.* ]]; then
  export LDFLAGS=${LDFLAGS_CC}
fi

export CFLAGS="-I${PREFIX}/include -L${PREFIX}/lib ${CFLAGS}"
${PYTHON} setup.py install --single-version-externally-managed --record=record.txt
