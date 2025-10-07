num = input("Enter a number: ")


length = len(num)
i = 0


while i < length - 1 and num[i] < num[i + 1]:
    i += 1

if i == 0 or i == length - 1:
    print("Not a hill number")
else:
    while i < length - 1 and num[i] > num[i + 1]:
        i += 1

    if i == length - 1:
        print("Hill number")
    else:
        print("Not a hill number")
