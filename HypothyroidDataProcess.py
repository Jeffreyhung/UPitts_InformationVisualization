hypo_file = open("data/hypothyroid.data", "r")
lines = hypo_file.readlines()
hypo_file.close()
hypo = []


# function for turning things into binary
def organize(temp):
    temp = [tem.replace('f', '0').replace('t', '1').replace('M', '1')
                .replace('F', '0').replace('y', '1').replace('n', '0')
            for tem in temp]
    return temp


# organize each
for i in lines:
    temp = (i.rstrip('\n').split(','))
    if (temp[1] != '?') and ( temp[2] != '?'):
        if temp[0] == 'hypothyroid':
            temp[0] = '1'
        else:
            temp[0] = '0'
        temp = organize(temp)
        hypo.append(temp)
# write into new data
new_file = open("data/HypothyroidProcessed.txt", "w")
for i in hypo:
    for j in i:
        new_file.write(str(j))
        new_file.write(" ")
    new_file.write('\n')
new_file.close()

