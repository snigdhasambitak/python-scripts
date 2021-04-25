### Given an array which may contain duplicates, print all elements and their frequencies

def array_frequency(arr):
    dic = {}
    for i in arr:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

arr = [10, 20, 20, 10, 10, 20, 5, 20 ]
actual_dic = array_frequency(arr)
for item in actual_dic:
    print(f'the frequency of {item} is {actual_dic[item]}')
