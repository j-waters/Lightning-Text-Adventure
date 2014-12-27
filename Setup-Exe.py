import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('LegendOfAiopaC1.py', base=base, compress=True)
]

setup(
    name = "Legend Of Aiopa",
    version = "0.1",
    description = "A text based adventure",
    executables = executables
    )
