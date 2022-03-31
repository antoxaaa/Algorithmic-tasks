n = input()
spisok = list(map(int, input().split()))

def symmetric(spisok):

    out_spisok = []

    for i in range(len(spisok)+1):
        seq = spisok+out_spisok
        if seq == seq[::-1] and spisok:
            print(len(out_spisok))
            print(*out_spisok)
            break
        else:
            out_spisok = [spisok[i]] + out_spisok

symmetric(spisok)