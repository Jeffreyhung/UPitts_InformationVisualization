# Read processed file
fertile_file = open("data/FertilityProcessed.txt", "r")
lines = fertile_file.readlines()
fertile_file.close()
fertile = []
for i in lines:
    temp = i.rstrip('\n').rstrip(' ').split(' ')
    temp = map(int, temp)
    fertile.append(temp)

# Function for getting every n-th item in fertile
def get_n_item(item):
    temp=[]
    for i in fertile:
        temp.append(i[int(item)])
    return temp



print get_n_item(1)