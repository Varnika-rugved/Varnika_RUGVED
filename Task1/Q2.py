text = input("Enter a string: ")


sorted_text = sorted(text)
print("Sorted string:", ''.join(sorted_text))


for char in sorted_text:
    count = sorted_text.count(char)
    print(char, ":", count)
