#!/usr/bin/python

# ====================================================================================
#  Experiment 3 from the paper
#  "Population-based vs. Single-solution heuristics for the Travelling Thief Problem"
# ====================================================================================

import os
import time

instances = [
  "eil51_n150_bounded-strongly-corr_01.ttp",
  "eil51_n150_uncorr_01.ttp"
]

# nb of iterations
n = 30

# test all instances
for instance in instances:
  for i in range(0,n):
    os.system("java -jar ttplab-optlog.jar "+instance+" ma2b ma2b-2016-10-03.csv")
    time.sleep(2)
