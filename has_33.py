#### FIND 33:

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False

def has_33(num_array):
    for i in range(0, (len(num_array)-1)):
        # This is good
        # if num_array[i] == num_array[i+1] == 3:

        # This is better
        if num_array[i:i+2] == [3,3]:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))