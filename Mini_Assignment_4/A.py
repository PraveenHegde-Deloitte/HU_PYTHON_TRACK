#lamda
eqn = lambda x, a, b, c: a * x * x + b * x + c

x = int(input("Enter value for x :"))
a = int(input("Enter  value for a :"))
b = int(input("Enter value for b :"))
c = int(input("Enter value for c :"))
print(eqn(x, a, b, c))
