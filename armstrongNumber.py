def armstrong():
    number = int(input("Enter number: "))
    number_len = len(str(number))
    if number <= 1:
        print("Enter a number greater than 1")
    elif number_len == 1:
        print("All single numbers are Armstrong numbers")
    else:
        sum_total = 0
        for digit in str(number):
            sum_total += int(digit) ** int(number_len)
        if sum_total == number:
            print("{} is an Armstrong number".format(number))
        else:
            print("{} is not an Armstrong number".format(number))


print("This program determines if the number entered is an Armstrong number")
armstrong()
