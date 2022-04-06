lst=[-1000, 500, -600, 700, 5000, -90000, -17500]
print(list)

negative=list(map(lambda x:abs(x),(filter(lambda x:x<0,map(lambda x:x,lst)))))
print(negative)