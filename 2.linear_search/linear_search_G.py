reader = open('linear_search_G.txt', 'r')
seq = [int(n) for n in reader.readline().split()]
reader.close()

seq_max = seq
seq_min = seq

if len(seq) == 2: 
    if seq[0] > seq[1]:
        print(seq[1],seq[0])
    else:
        print(seq[0],seq[1])
else:
    max1 = max(seq_max)
    ind_1 = seq_max.index(max1)
    seq_max.pop(ind_1)
    max2 = max(seq_max)

    min1 = min(seq_min)
    ind_3 = seq_min.index(min1)
    seq_min.pop(ind_3)
    min2 = min(seq_min)

    if max1*max2 > min1*min2:
        if max1 > max2:
            print(max2,max1)
        else:
            print(max1,max2)
    elif max1*max2 < min1*min2:
        if min1 > min2:
            print(min2,min1)
        else:
            print(min1,min2)
    else:
        if max1 > max2:
            print(max2,max1)
        else:
            print(max1,max2)
            