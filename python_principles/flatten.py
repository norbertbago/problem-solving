def flatten(list1):
    result = []
    for list_item in list1:
        for item in list_item:
            result.append(item)
    return result
            