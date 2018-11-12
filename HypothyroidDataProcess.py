hypo_file = open("data/hypothyroid.data", "r")
lines = hypo_file.readlines()
hypo_file.close()
temp = []
hypo = []
for i in lines:
    temp = (i.rstrip('\n').split(','))
    if (temp[1] != '?') and ( temp[2] != '?'):
        temp = [t.replace('f', '0') for t in temp]
        temp = [t.replace('t', '1') for t in temp]
        if temp[0] == 'hypothyroid':
            temp[0] = 1
        else:
            temp = 0
        hypo.append(temp)

# words = [w.replace('[br]', '<br />') for w in words]

print hypo
print len(hypo)

