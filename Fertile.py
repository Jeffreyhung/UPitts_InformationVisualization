fertile_file = open("data/fertility.txt", "r")
lines = fertile_file.readlines()
fertile_file.close()
new_file = open("data/processed.txt", "w")
j = 0
temp=[]
fertile = []
for i in lines:
    temp = (i.rstrip('\n').split(','))
    temp[0] = int(round((float(temp[0])+1)*1.5))
    temp[1] = int(float(temp[1])*18+18)
    temp[5] = int(int(temp[5])+1)
    temp[6] = int(float(temp[6])*5)
    temp[7] = int(int(temp[5]) + 1)
    temp[8] = int(float(temp[8])*18)
    if (temp[9] == 'N'):
        temp[9] = 0
    else:
        temp[9] = 1
    fertile.append(temp)
    new_file.write(str(temp)+"\n")


print fertile
new_file.close()
