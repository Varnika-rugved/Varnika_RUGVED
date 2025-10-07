arr = [10,3, 5, 3, 4, 3, 5, 6]

first_repeat = -1
for i in range(len(arr)):

    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            first_repeat = arr[i]
            break
    if first_repeat != -1:
        break
if first_repeat != -1:
    print("First repeating element is:", first_repeat)
else:
    print("No repeating element found")
