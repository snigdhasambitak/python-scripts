###Given a number, find the sum of its digits. Take the number as an input from the user


def sum_of_digits():
    return(sum([int(i) for i in input("enter the  num")]))

print(sum_of_digits())