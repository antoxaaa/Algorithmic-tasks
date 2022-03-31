reader = open('linear_search_A.txt', 'r')
spisok = []
spisok = [int(n) for n in reader.readline().split(" ")]
reader.close()



def find_posled(spisok):
    answer = "NO"
    i = 1
    while i != len(spisok) and spisok[i-1] < spisok[i]:
        i += 1
            
    if  i == len(spisok):
        answer = "YES"

    print(answer)

find_posled(spisok)