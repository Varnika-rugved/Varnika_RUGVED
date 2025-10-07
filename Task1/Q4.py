def selection_sort_string(s):
    letters = []
    for c in s:
        letters.append(c)
        n = len(letters)

    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if letters[j] < letters[min_pos]:
                min_pos = j
        temp = letters[i]
        letters[i] = letters[min_pos]
        letters[min_pos] = temp
    sorted_s = ""
    for c in letters:
        sorted_s += c

    return sorted_s

text = input("Enter a string: ")
print("Sorted string:", selection_sort_string(text))
