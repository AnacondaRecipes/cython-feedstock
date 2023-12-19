import sys
import platform
is_cpython = platform.python_implementation() == 'CPython'

import Cython
import Cython.Build
import Cython.Compiler
import Cython.Compiler.Code
import Cython.Compiler.FlowControl
import Cython.Compiler.Lexicon
import Cython.Compiler.Parsing
import Cython.Compiler.Scanning
import Cython.Compiler.Visitor
import Cython.Plex.Actions
import Cython.Plex.Scanners
import Cython.Runtime
import Cython.Distutils
import Cython.Debugger
import Cython.Debugger.Tests
import Cython.Plex
import Cython.Tests
import Cython.Build.Tests
import Cython.Compiler.Tests
import Cython.Utility
import Cython.Tempita

import pyximport

if is_cpython:
    import Cython.Runtime.refnanny

import sys
import os
import subprocess
from pprint import pprint

pprint('sys.executable: %r' % sys.executable)
pprint('sys.prefix: %r' % sys.prefix)
pprint('sys.version: %r' % sys.version)
pprint('PATH: %r' % os.environ['PATH'])
pprint('CWD: %r' % os.getcwd())

from setuptools import setup, Extension
from Cython.Distutils import build_ext
from shutil import which as find_executable


if find_executable('gcc') or find_executable('clang'):
    sys.argv[1:] = ['build_ext', '--inplace']
    setup(name='fib',
        cmdclass={'build_ext': build_ext},
        ext_modules=[Extension("fib", ["fib.pyx"])])

    try:
        import fib
        assert fib.fib(10) == 55
    except ImportError:
        cmd = [sys.executable, '-c', 'import fib; print(fib.fib(10))']
        out = subprocess.check_output(cmd)
        assert out.decode('utf-8').strip() == '55'
