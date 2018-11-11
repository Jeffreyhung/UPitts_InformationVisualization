import matplotlib.pyplot as plt
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
def get_n_item(item):
    tmp = []
    for x in fertile:
        tmp.append(x[int(item)])
    return tmp

'''
def scatterplot(a, b, title="", color = "r"):
    x_data = get_n_item(a)
    y_data = get_n_item(b)
    n_data = get_n_item(9)
    x_label = nameSet[a]
    y_label = nameSet[b]

    # Create the plot object
    _, ax = plt.subplots()

    # s size, c color, marker type of dot, alpha transparency
    ax.scatter(x_data, n_data, s = 10, c = 'red', alpha = 0.3, marker='x', label = x_label)
    ax.scatter(y_data, n_data, s = 10, c = 'green', alpha = 0.3, marker='o', label = y_label)

    # Label the axes and provide a title
    title = 'Scatterplot of ',x_label,' and ',y_label
    ax.set_title(title)
    ax.set_ylabel(nameSet[9])
    ax.legend(loc='upper right')
    plt.show()


scatterplot(6,5)
'''