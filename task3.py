# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящих N,
# в порядке возрастания.

if __name__ == '__main__':
    from math import *
    n = int(input())
    num = 1
    while n >= num:
        if sqrt(num) == int(sqrt(num)):
            print(num)
        num += 1