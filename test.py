#!/usr/bin/python
import os

# test one instance: a280_n279_bounded-strongly-corr_01.ttp
# run algorithm MA2B for at most 30 sec
# and save the result in output/my-results.txt
os.system("java -jar ttplab.jar a280_n279_bounded-strongly-corr_01.ttp cs2sa my-results.txt 30")
