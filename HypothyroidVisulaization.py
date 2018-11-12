import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
hypo_file = open("data/HypothyroidProcessed.txt", "r")
lines = hypo_file.readlines()
hypo_file.close()
hypo = []
nameSet = []
# Remove space and '\n' and split by space, store data in fertile array
for i in lines:
    temp = i.rstrip(' \n').split(' ')
    temp = map(int, temp)
    hypo.append(temp)

print hypo