#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from PIL import Image
import glob
import re
import os
import argparse
from copy import copy


parser = argparse.ArgumentParser(description='Resize images')

parser.add_argument('-f', dest='f', action='store',
                    help='Mask for input files', required=True)
parser.add_argument('-o', dest='o', action='store', default=".",
                    help='Output folder')
parser.add_argument('-s', dest='s', action='store', required=True,
                    help='Size for resizing, format WхH. Where W and H may be a number (for hard resize), '+\
                    'float number for percentage resize or "p" for the proportional resize')
parser.add_argument('-n', dest='n', action='store', default="{on}.{ext}",
                    help='New name for files. Can contain formating. For example, "image{n}.png"\n'+\
                    "You can use:, "+\
                    "n -- number, " +\
                    "ext -- extension, " +\
                    "on -- old name of file, " +\
                    "and other str.format() features" )

#parser.add_argument('-', dest='', action='store',
#                    help='')

args = parser.parse_args()


input_files = glob.glob(args.f)
output = args.o.replace("\\", "/") if (args.o.endswith("/") or args.o.endswith("\\")) else args.o.replace("\\", "/") + "/"
size_raw = args.s.lower().split("x")
new_name = args.n

for i, s in enumerate(size_raw):
    if s.replace(".", "").isdigit():
        if "." in s:
            size_raw[i] = float(s)
        else:
            size_raw[i] = int(s)
    elif s != "p":
        raise ValueError("Wrong size (-s)")
if size_raw[0] == size_raw[1] == "p":
    raise ValueError("Size can't be pxp")


if not os.path.exists(output):
    cur_dir = os.getcwd()
    for d in output.split("/"):
        if not d:
            continue
        if not os.path.exists(d):
            os.mkdir(d)
        os.chdir(d)
    os.chdir(cur_dir)

for i, f in enumerate(input_files):
    ol = f.replace("\\", "/").split("/")[-1]
    on, ext = os.path.splitext(ol)
    ext = ext.replace(".", "")

    im = Image.open(f)
    o_size = copy(list(im.size))
    end_size = copy(list(im.size))
    #for si, s in enumerate(size_raw):
    if type(size_raw[0]) == int:
        end_size[0] = size_raw[0]
    elif type(size_raw[0]) == float:
        end_size[0] = round(end_size[0] * size_raw[0])
    
    if type(size_raw[1]) == int:
        end_size[1] = size_raw[1]
    elif type(size_raw[1]) == float:
        end_size[1] = round(end_size[1] * size_raw[1])
    
    
    if size_raw[0] == "p":
        r = o_size[0] / o_size[1]
        end_size[0] = round(end_size[1]*r)
    if size_raw[1] == "p":
        r = o_size[1] / o_size[0]
        print(r)
        end_size[1] = round(end_size[0]*r)

    im.resize(end_size).save(output + new_name.format(on=on, ext=ext, n=i))

        

