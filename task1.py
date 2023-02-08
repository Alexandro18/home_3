#По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания

if __name__ == '__main__':

    n = int(input())
    deg = 0
    while n > 0:
        if 2 ** deg <= n:
            print(2 ** deg, end =' ')
            deg +=1
        else:
            break