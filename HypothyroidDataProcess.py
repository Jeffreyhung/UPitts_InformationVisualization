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
    '''
    [00] Result              0 false  1 true
    [01] Age                 age (int)
    [02] Sex                 0 Female  1 Male
    [03] on thyroxine        0 false  1 true
    [04] query on thyroxine  0 false  1 true
    [05] on Anti-thyroid     0 false  1 true
    [06] Surgery             0 false  1 true
    [07] Query Hypothyroid   0 false  1 true
    [08] Query Hyperthyroid  0 false  1 true
    [09] Pregnant            0 normal, 1 altered
    [10] Sick                0 false  1 true
    [11] Tumor               0 false  1 true
    [12] Lithium             0 false  1 true
    [13] Goitre              0 false  1 true
    [14] TSH    0 false  1 true
    [15]        Num of TSH / int or '?'
    [16] T3     0 false  1 true
    [17]        Num of T3 / int or '?'
    [18] TT4    0 false  1 true
    [19]        Num of TT4 / int or '?'
    [20] T40    0 false  1 true
    [21]        Num of T40 / int or '?'
    [22] FTI    0 false  1 true
    [23]        Num of FTI / int or '?'
    [24] TBG    0 false  1 true
    [25]        Num of TBG / int or '?'
    '''
# write into new data
new_file = open("data/HypothyroidProcessed.txt", "w")
for i in hypo:
    for j in i:
        new_file.write(str(j))
        new_file.write(" ")
    new_file.write('\n')
new_file.close()

