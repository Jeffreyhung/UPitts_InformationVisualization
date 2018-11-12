hypo_file = open("data/hypothyroid.data", "r")
lines = hypo_file.readlines()
hypo_file.close()
temp = []
hypo = []
for i in lines:
    temp = (i.rstrip('\n').split(','))
    #boo = 0
    #boo = "?" in temp
    if (temp[1] != '?' ) and ( temp[2] != '?'):
        hypo.append(temp)

#print hypo
print len(hypo)

