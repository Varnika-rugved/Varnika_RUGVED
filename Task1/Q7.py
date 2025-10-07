n = int(input("Enter how many terms: "))
a = 0
b = 1
if n == 1:
    print(a)
else:
    print("Fibonacci sequence:")
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
