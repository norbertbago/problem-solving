def all_equal(lst):
    if lst == []:
        return True
    else:
        n = lst[0]
        for i in lst:
            if i != n:
                return False
        return True