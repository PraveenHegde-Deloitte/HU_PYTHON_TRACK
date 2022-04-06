#map,count and lamda

lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

#No of A and a
counting_A=list(map(lambda x:x.count("A"),lst1))
counting_a=list(map(lambda x:x.count("a"),lst1))

#printing No of A and a
print(counting_A)
print(counting_a)

#printing combo
c=list(map(lambda x,y:[x,y],counting_a,counting_A))
print(c)




