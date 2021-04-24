# Given a number, check whether the given number is an Armstrong number or not. A positive integer is called an Armstrong number of order n if:

# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

# 153 is an Armstrong number of order 3
# Inputs from the user will be number and order n.

def armstrong():
    num = int(input("enter a num"))
    num_list = list(map(int, str(num)))
    n = int(input(f"enter the order, which should be {len(num_list)}"))
    sum = 0
    for i in num_list:
        sum += i ** n
    if sum == num:
        print(f'{num} is an armstrong number')
    else:
        print(f'{num} is not an armstrong number')

armstrong()


