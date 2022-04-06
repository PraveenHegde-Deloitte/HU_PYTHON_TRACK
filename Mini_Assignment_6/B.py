def fib(num):
    x = 0
    y = 1
    for i in range(num):
        yield x
        # Adds values together then swaps them
        x, y = y, x + y

n=int(input('Enter for n: '))
for z in fib(n):
    print(z)
