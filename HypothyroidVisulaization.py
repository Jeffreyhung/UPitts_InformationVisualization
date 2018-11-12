import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
hypo_file = open("data/HypothyroidProcessed.txt", "r")
lines = hypo_file.readlines()
hypo_file.close()
hypo = []
nameSet = []
# Remove space and '\n' and split by space, store data in hypo array
for i in lines:
    temp = i.rstrip(' \n').split(' ')
    for x in range(14):
        temp[x] = int(temp[x])
    for x in range(14, 26, 2):
        temp[x] = int(temp[x])
        if temp[x]:
            temp[x+1] = float(temp[x+1])
    hypo.append(temp)

print hypo
