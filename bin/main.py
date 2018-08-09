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
	opt  = line.split()[0]
	if opt in "INT1":
		int1 = int(line.split()[1])
		print "init1 :" + str(int1)
	elif opt in "REAL1":
		real1 = float(line.split()[1])
		print "real1 :" + str(real1)
	elif opt in "LIST1":
		list1 = line.split()[1]
		print "list1 :" + list1
	elif opt in "VECTOR1":
		vector1 = map(int, line.split("[")[1].split(']')[0].split())
		print "vector1 :" + str(vector1)
	else:
		print "SDE value read error. your input key is " + str(opt)
		sys.exit(1)

f_sde.close()
