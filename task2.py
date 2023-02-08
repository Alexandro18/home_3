# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки,
# или слово NO в противном случае

if __name__ == '__main__':

    n = int(input())
    deg = 0
    while n > 0:
        if 2 ** deg == n:
            print('YES')
            break
        elif 2 ** deg > n:
            print('NO')
            break
        deg +=1