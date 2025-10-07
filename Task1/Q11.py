text = input("Enter your text: ")

letters = 0
words = 1
sentences = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch == ' ':
        words += 1
    elif ch in ['.', '!', '?']:
        sentences += 1
L = (letters / words) * 100
S = (sentences / words) * 100

index = 0.0588 * L - 0.296 * S - 15.8
grade = round(index)

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print("Grade", grade)

