import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Read processed file
fertile_file = open("data/FertilityProcessed.txt", "r")
lines = fertile_file.readlines()
fertile_file.close()
fertile = []
nameSet = ['Season', 'Age', 'Disease', 'Trauma', 'Surgical', 'Fever', 'Alcohol', 'Smoke', 'Sitting Hour', 'Result']
# Remove space and '\n' and split by space, store data in fertile array
for i in lines:
    temp = i.rstrip(' \n').split(' ')
    temp = map(int, temp)
    fertile.append(temp)

# Separate Normal and Altered data
normal_data = []
altered_data = []
for i in fertile:
    if i[9]:
        altered_data.append(i)
    else:
        normal_data.append(i)


# count the percentage of disease, trauma and surgical
def statistic (data, target):
    for i in data:
        if i[2]:
            target[0] += 1

        if i[3]:
            target[1] += 1

        if i[4]:
            target[2] += 1

    for i in range(3):
        target[i] = (target[i]*100/len(data))


# Sum the number of disease, trauma and surgical
normal_statistic = [0, 0, 0]
altered_statistic = [0, 0, 0]

statistic(normal_data, normal_statistic)
statistic(altered_data, altered_statistic)
print normal_statistic
print altered_statistic





#  Function for getting every n-th item in fertile
def get_n_item(item, array=fertile):
    tmp = []
    for x in array:
        tmp.append(x[int(item)])
    return tmp


def scatter_plot(a, b):
    x_data_n = get_n_item(a, normal_data)
    x_data_a = get_n_item(a, altered_data)
    y_data_n = get_n_item(b, normal_data)
    y_data_a = get_n_item(b, altered_data)
    x_label = nameSet[a]
    y_label = nameSet[b]
# Create the plot object
    fig, ax = plt.subplots()
# create a list of the sizes, here multiplied by 10 for scale
    c = Counter(zip(x_data_n, y_data_n))
    s = [50 * c[(xx, yy)] for xx, yy in zip(x_data_n, y_data_n)]
# s size, c color, marker type of dot, alpha transparency
    ax.scatter(x_data_n, y_data_n, s = s, c = 'blue', alpha = 0.75, marker='o', label = "Normal")
    c = Counter(zip(x_data_a, y_data_a))
    s = [50 * c[(xx, yy)] for xx, yy in zip(x_data_a, y_data_a)]
    ax.scatter(x_data_a, y_data_a, s = s, c = 'red', alpha = 0.75, marker='s', label = "Altered")
# Label the axes and provide a title
    title = 'Scatterplot of ',x_label,' and ',y_label
    ax.set_title(title)
    ax.set_xlabel(nameSet[a])
    ax.set_ylabel(nameSet[b])
    ax.legend(loc='best', markerscale=0.5, markerfirst=0)
    plt.show()


def bar_chart(dataset1, dataset2):
# Create the plot object
    fig, ax = plt.subplots()

    index = np.arange(3)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    ax.bar(index, dataset1, bar_width, alpha=opacity, color='b', error_kw=error_config, label='Normal')
    ax.bar(index + bar_width, dataset2, bar_width, alpha=opacity, color='r', error_kw=error_config, label='Altered')

    ax.set_xlabel('Group')
    ax.set_ylabel('Percentage')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(('Disease', 'Trauma', 'Surgical'))
    ax.legend()

    fig.tight_layout()
    plt.show()


bar_chart(normal_statistic, altered_statistic)
scatter_plot(2,3)
scatter_plot(1,8)