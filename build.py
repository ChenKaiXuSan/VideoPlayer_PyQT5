# - *- encoding: utf-8 -*-
'''
use PyInstaller to build the .py file to .exe.
'''

import PyInstaller.__main__ as main

main.run([
    'main.py',
    '--onefile',
    '--windowed',
    '--distpath=.' # compile path
])
