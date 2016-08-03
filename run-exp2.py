#!/usr/bin/python

# ====================================================================================
#  Experiment 2 from the paper
#  "Population-based vs. Single-solution heuristics for the Travelling Thief Problem"
# ====================================================================================

import os
import time

nb_cities = 4461
base_instance = 'fnl4461'

kp_types = ['bounded-strongly-corr','uncorr-similar-weights','uncorr']
kp_cat = ['01','05','10']
item_factor = [1,5,10]

# test all instances
for t in kp_types:
  for c in kp_cat:
    for f in item_factor:
      instance = base_instance + "_n" + str((nb_cities-1)*f) + "_" + t + "_" + c + ".ttp"
      os.system("java -jar ttplab.jar "+instance+" cs2sa exp2-fnl4461-CS2SA.csv")
      time.sleep(5)
