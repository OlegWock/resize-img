#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from shutil import copyfile
import os

copyfile(os.path.dirname(os.path.realpath(__file__))+"/main.py", os.path.expanduser("~/.scripts/resizeimg"))
os.system("chmod +x ~/.scripts/resizeimg")