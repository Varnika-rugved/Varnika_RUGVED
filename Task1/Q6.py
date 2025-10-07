def is_anagram(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    list1 = []
    for ch in str1:
        list1.append(ch)

    list2 = []
    for ch in str2:
        list2.append(ch)

    list1.sort()
    list2.sort()
    if list1 == list2:
        print("Both strings are anagrams")
    else:
        print("Not anagrams")
a = input("Enter first string: ")
b = input("Enter second string: ")

is_anagram(a, b)
