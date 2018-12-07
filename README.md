# Run one TTP instance

## Prerequisites:
- java 1.7+
- a linux OS

## Command:
    java -jar ttplab.jar <instance_name> <algo_name> <output_filename> <max_runtime>

- instance_name : TTP instance name, eg. eil76_n750_uncorr_10.ttp
- algo_name : algorithm to run, 3 algorithms are available: cs2b [2], cs2sa [1], and ma2b [1]
- output_filename [optional] : output file name, default is: <algo_name>.csv
- max_runtime [optional] : maximum runtime in seconds, default is 600 sec

## Output:
- objective value and runtime is saved in the output/ folder
- best found solution is saved in a file in output/solutions/

## Example:
    java -jar ttplab.jar eil76_n750_uncorr_10.ttp ma2b output.txt 100


# Run all instances from [1]

## Prerequisites:
- python 2.7
- java 1.7+
- a linux OS

## Command:
    ./run.py


# Algorithms/References

- cs2b  : CoSolver-based with 2-OPT and Bit-flip [2]
- cs2sa : CoSolver-based with 2-OPT and Simulated Annealing [1]
- ma2b  : Memetic Algorithm with 2-OPT and Bit-flip [1]

[1] Mohamed El Yafrani, and Belaïd Ahiod. "Population-based vs. Single-solution Heuristics for the Travelling Thief Problem." Proceedings of the 2016 on Genetic and Evolutionary Computation Conference. ACM, 2016.

[2] Mohamed El Yafrani, and Belaïd Ahiod. "Cosolver2B: An Efficient Local Search Heuristic for the Travelling Thief Problem." arXiv preprint arXiv:1603.07051 (2016).


# Important notes

1. make sure all the python scripts and the files in bins directory are executable:
   chmod +x *.py bins -R

2. due to space constraint, TTP data are removed from the database directory,
   except for a280-based instances. TTP instances are available at:
   http://cs.adelaide.edu.au/~optlog/CEC2014COMP_InstancesNew/

3. the linkern binary file in the bins/linkern/ folder is a modified one.
   The source codes have been slightly hacked in order to improve the randomness of
   the generated initial tours

4. there was a metric issue in the older version (before Nov 14, 2016), please consider the current version for comparison purposes
