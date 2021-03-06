import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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

# Separate Normal data and Hypothyroid Data
normal_data = []
hypothyroid_data = []
for i in hypo:
    if i[0]:
        hypothyroid_data.append(i)
    else:
        normal_data.append(i)


# count the percentage of each item
def statistic (data, target):
    for i in data:
        for j in range(2, 14):
            if i[j]:
                target[j-2] += 1
        for j in range(14, 25, 2):
            if i[j]:
                target[j-2] += 1
    for i in range(len(target)):
        target[i] = (target[i]*100/len(data))
    return target


# Sum the number of disease, trauma and surgical
normal_statistic = [0]*26
hypothyroid_statistic = [0]*26

normal_statistic = statistic(normal_data, normal_statistic)
hypothyroid_statistic = statistic(hypothyroid_data, hypothyroid_statistic)

def bar_chart(dataset1, dataset2, x_label):
    fig, ax = plt.subplots()
# parameter setting
    index = np.arange(len(dataset1))
    bar_width = 0.35
    opacity = 0.4
# input data
    ax.bar(index, dataset1, bar_width, alpha=opacity, color='b', label='Normal')
    ax.bar(index + bar_width, dataset2, bar_width, alpha=opacity, color='r', label='Abnormal')
# Label the axes
    ax.set_ylabel('Percentage')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(x_label)
    ax.legend()
# Show chart
    fig.tight_layout()
    plt.show()


def pie_chart(data, labels):
    colors = ['lightskyblue', 'lightcoral']
    explode = (0.03, 0)  # explode 1st slice
    # Plot
    plt.pie(data, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.axis('equal')
    plt.show()


def count_chart(dataset):
    sns.set(style="white")
    ax = sns.countplot(x = 'age', hue = 'type', data=dataset)
    plt.show()


count_chart({'age': [i[1] for i in hypo], 'type': [i[0] for i in hypo]})
pie_chart([len(normal_data), len(hypothyroid_data)],['Normal', 'Hypothyroid'])
bar_chart(normal_statistic[1:11:], hypothyroid_statistic[1:11:], ('On Thyroxine', 'Query on Thyroxine',
          'On Anti-Thyroid', 'Query Hypothyroid', 'Query Hyperthyroid', 'Pregnant', 'Sick', 'Tumor', 'Lithium', 'Goitre'))
pie_chart([hypothyroid_statistic[0], len(hypothyroid_data)-hypothyroid_statistic[0]], ['Men', 'Women'])
bar_chart(normal_statistic[12:23:2], hypothyroid_statistic[12:23:2],('TSH', 'T3', 'TT4', 'T4U', 'FTI', 'TBG') )

