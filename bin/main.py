#!/usr/local/bin/python
""" EDISON python sample code"""

import sys
import os
import getopt
import math
import numpy as np


try:
    otps, args = getopt.getopt(sys.argv[1:], "i:")
except getopt.GetoptError as err:
    print(str(err))
    sys.exit(1)

for opt, arg in otps:
    if opt in "-i":
        f_sde = open(arg, "r")

print("input file = " + f_sde.name)
sde_lines = f_sde.readlines()

for line in sde_lines:
    opt = line.split()[0]
    if opt in "a":
        a = float(line.split()[1])
        print("init1 : " + str(a))
    elif opt in "b":
        b = float(line.split()[1])
        print("b : " + str(b))
    elif opt in "c":
        c = float(line.split()[1])
        print("c : " + str(c))
    elif opt in "d":
        d = float(line.split()[1])
        print("d : " + str(d))
    else:
        print("Inputdeck value read error. your input key is " + str(opt))
        sys.exit(1)

f_sde.close()
