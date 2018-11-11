import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import seaborn
import pandas

# Read processed file
fertile_file = open("data/FertilityProcessed.txt", "r")
lines = fertile_file.readlines()
fertile_file.close()
fertile = []
for i in lines:
    temp = i.rstrip(' \n').split(' ')
    temp = map(int, temp)
    fertile.append(temp)
nameSet = ['Season','Age','Disease', 'Trauma', 'Surgical','Fever','Alcohol', 'Smoke', 'Sitting Hour', 'Result']

# Separate Normal and Altered data
normal_data = []
altered_data = []
for i in fertile:
    if i[9]:
        altered_data.append(i)
    else:
        normal_data.append(i)


# Function for getting every n-th item in fertile
def get_n_item(item, array=fertile):
    tmp = []
    for x in array:
        tmp.append(x[int(item)])
    return tmp


def scatterplot(a, b):
    x_data_n = get_n_item(a, normal_data)
    x_data_a = get_n_item(a, altered_data)
    y_data_n = get_n_item(b, normal_data)
    y_data_a = get_n_item(b, altered_data)
    x_label = nameSet[a]
    y_label = nameSet[b]
# Create the plot object
    _, ax = plt.subplots()
# create a list of the sizes, here multiplied by 10 for scale
    c = Counter(zip(x_data_n, y_data_n))
    s = [50 * c[(xx, yy)] for xx, yy in zip(x_data_n, y_data_n)]
# s size, c color, marker type of dot, alpha transparency
    ax.scatter(x_data_n, y_data_n, s = s, c = 'red', alpha = 0.75, marker='o', label = "Normal")
    c = Counter(zip(x_data_a, y_data_a))
    s = [50 * c[(xx, yy)] for xx, yy in zip(x_data_a, y_data_a)]
    ax.scatter(x_data_a, y_data_a, s = s, c = 'blue', alpha = 0.75, marker='x', label = "Altered")
# Label the axes and provide a title
    title = 'Scatterplot of ',x_label,' and ',y_label
    ax.set_title(title)
    ax.set_xlabel(nameSet[a])
    ax.set_ylabel(nameSet[b])
    ax.legend(loc='upper right')
    plt.show()



scatterplot(6,5)