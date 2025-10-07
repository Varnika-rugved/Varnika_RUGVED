string = input("Enter a string: ")
n = int(input("Enter number of characters in each part: "))

length = len(string)

if length % n != 0:
    print("Cannot divide string equally.")
else:
    parts = []
    for i in range(0, length, n):
        part = string[i:i + n]
        parts.append(part)
    first_part = parts[0]
    same = True
    for p in parts:
        if p != first_part:
            same = False
            break

    if same:
        print("Equal parts are:")
        for p in parts:
            print('"' + p + '"')
    else:
        print("Sequence is not same in all parts.")

