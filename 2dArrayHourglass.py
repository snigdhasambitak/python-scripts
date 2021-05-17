# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

# Example


# -9 -9 -9  1 1 1 
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
# The  hourglass sums are:

# -63, -34, -9, 12, 
# -10,   0, 28, 23, 
# -27, -11, -2, 10, 
#   9,  17, 25, 18
# The highest hourglass sum is  from the hourglass beginning at row , column :

# 0 4 3
#   1
# 8 6 6



def hourglassSum(arr):
    
    new_arr = [[0]*(len(arr[0])-2) for i in range(len(arr)-2)]

    largest = -sys.maxsize - 1
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            if i in range(0,6) and j in range(0,6) and arr[i][j] in range(-9,10):
                 sum = 0
                 for k in range(0,3):
                    sum += arr[i][j+k] + arr[i+2][j+k]
                 new_arr[i][j] = arr[i+1][j+1] + sum
                 if new_arr[i][j] > largest :
                    largest = new_arr[i][j]
    print(new_arr)    
    return largest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
 
