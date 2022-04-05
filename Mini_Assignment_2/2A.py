input = int(input('Input number of rows: '))
a = 0
row = []
while a < input:
    b = 11 ** a
    k=len(str(b))
    for p in range(input-k):
        b=b*10
    row.append(b)
    a += 1
for i in range(0,len(row)):
    row[i] = str(row[i])
    print(row[i])
