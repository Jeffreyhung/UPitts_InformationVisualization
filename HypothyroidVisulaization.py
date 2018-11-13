import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
hypo_file = open("data/HypothyroidProcessed.txt", "r")
lines = hypo_file.readlines()
hypo_file.close()
hypo = []
nameSet = ['Result', 'Age', 'Sex', 'On Thyroxine', 'Query on Thyroxine', 'On Anti-Thyroid', 'Query Hypothroid',
           'Query Hyperthyroid', 'Pregnant', 'Sick', 'Tumor', 'Lithium', 'Goitre',
           'TSH Measure', 'TSH', 'T3 Measure', 'T3', 'TT4 Measure', 'TT4',
           'T40 Measure', 'T40', 'FTI Measure', 'FTI', 'TBG Measure', 'TBG']
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

def bar_chart(dataset1, dataset2):
    fig, ax = plt.subplots()
# parameter setting
    index = np.arange(3)
    bar_width = 0.35
    opacity = 0.4
# input data
    ax.bar(index, dataset1, bar_width, alpha=opacity, color='b', label='Normal')
    ax.bar(index + bar_width, dataset2, bar_width, alpha=opacity, color='r', label='Altered')
# Label the axes
    ax.set_ylabel('Percentage')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(('Disease', 'Trauma', 'Surgical'))
    ax.legend()
# Show chart
    fig.tight_layout()
    plt.show()
