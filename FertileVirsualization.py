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
    temp = i.rstrip('\n').rstrip(' ').split(' ')
    temp = map(int, temp)
    fertile.append(temp)
nameSet = ['Season','Age','Disease', 'Trauma', 'Surgical','Fever','Alcohol', 'Smoke', 'Sitting Hour', 'Result']

# Function for getting every n-th item in fertile
def get_n_item(item):
    temp=[]
    for i in fertile:
        temp.append(i[int(item)])
    return temp


colors = (0,0,0)
area = np.pi*3
plt.scatter(get_n_item(1), get_n_item(8), s=area, c=colors, alpha=0.5)
plt.show()

def scatterplot(x_data, y_data, x_label="", y_label="", title="", color = "r", yscale_log=False):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s = 10, color = color, alpha = 0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


'''
df = pandas.DataFrame(fertile, columns = nameSet)
seaborn .set()
seaborn.pairplot(df, hue="Result")
'''