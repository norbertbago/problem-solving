num = 2718

def AdditivePersistence(num):
    list_num = list(str(num))
    int_list = list(map(lambda x: int(x), list_num))
    len_lst  = len(list_num)
    sum_list = sum(int_list)

    if len_lst == 1:
        return sum_list
    else:
        return AdditivePersistence(sum_list)

print(AdditivePersistence(num))