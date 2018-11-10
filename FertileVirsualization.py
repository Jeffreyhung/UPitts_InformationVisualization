fertile_file = open("data/FertilityProcessed.txt", "r")
lines = fertile_file.readlines()
fertile_file.close()
fertile=[]
for i in lines:
    fertile.append(i.rstrip('\n').split(','))

print fertile


def getNitem():
    temp=[]
