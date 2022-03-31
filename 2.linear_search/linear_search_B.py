reader = open('linear_search_B.txt', 'r')
spisok = []
spisok = [int(n) for n in reader.readlines()]
reader.close()

def posled(spisok):
    ans = "RANDOM"

    i = 1
    const = 0
    ascen = 0
    desc = 0
    weak_ascen = 0
    weak_desc = 0

    while spisok[i] != (-2 * 10 ** 9):
        
        if spisok[i] == spisok[i-1]:
            const += 1
            weak_ascen += 1
            weak_desc += 1
        
        elif spisok[i] > spisok[i-1]:
            ascen += 1
            weak_ascen += 1       
            
        elif spisok[i] < spisok[i-1]:
            desc += 1
            weak_desc += 1       
        i += 1

    if (i-1) == const:
        ans = "CONSTANT"
    elif ascen == (i-1):
        ans = "ASCENDING"
    elif weak_ascen == (i-1):
        ans = "WEAKLY ASCENDING"
    elif desc == (i-1):
        ans = "DESCENDING"
    elif weak_desc == (i-1):
        ans = "WEAKLY DESCENDING"       

    print(ans)

posled(spisok)