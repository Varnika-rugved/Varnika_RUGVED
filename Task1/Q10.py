def check_card(number):
    number = number.replace(" ", "")

    digits = []
    for d in number:
        digits.append(int(d))

    total = 0
    reverse_digits = digits[::-1]

    for i in range(len(reverse_digits)):
        current = reverse_digits[i]
        if i % 2 == 1:
            current = current * 2
            if current > 9:
                current = current - 9
        total = total + current
    if total % 10 == 0:
        print("Valid credit card number")
    else:
        print("Invalid credit card number")
num = input("Enter credit card number: ")
check_card(num)
