fertile_file = open("data/fertility.txt", "r")
lines = fertile_file.readlines()
fertile_file.close()
new_file = open("data/FertilityProcessed.txt", "w")
j = 0
temp=[]
fertile = []
for i in lines:
    temp = (i.rstrip('\n').split(','))
    temp[0] = int(round((float(temp[0])+1)*1.5))
    temp[1] = int(float(temp[1])*18+18)
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    temp[4] = int(temp[4])
    temp[5] = abs(int(int(temp[5])+1)-2)
    temp[6] = abs(int(float(temp[6])*5)-5)
    temp[7] = int(temp[7])+1
    temp[8] = int(float(temp[8])*18)
    if (temp[9] == 'N'):
        temp[9] = 0
    else:
        temp[9] = 1
    fertile.append(temp)
    new_file.write(str(temp)+"\n")
    '''
    [0] Season      0 winter,  1 spring,  2 summer,  3 fall
    [1] Age         age (integer)
    [2] Disease     0 false  1 true
    [3] Trauma      0 false  1 true
    [4] Surgical    0 false  1 true
    [5] Fever       0 never, 1 more than 3 months,  2 less than 3 month
    [6] Alcohol     4 n/day, 3 1/day, 2 n/week, 1 1/week, 0 never
    [7] Smoke       0 never, 1 sometime, 2 daily
    [8] Sit Hour    hours(integer)
    [9] Result      0 normal, 1 altered
    '''

print fertile
new_file.close()
