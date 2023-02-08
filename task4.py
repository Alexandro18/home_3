# Шахматы ферзь

if __name__ == '__main__':

    a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
    if a1 == a2 or b1 == b2 or (a2 - a1) == (b1 - b2) or (a1 == b1 and a2 == b2) or (a2 - a1) == (b2 - b1):
        print('YES')
    else:
        print('NO')