# Write code for algorithm 3 below
def fibbonacci(n):
    if n == 1:
        return 0

    if n <= 2:
        return 1

    else:
        return fibbonacci(n-1)+fibbonacci(n-2)


print(fibbonacci(4))
