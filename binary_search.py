def binarysearch(list,element):
    """
    >>> binary_search(["a","b","c",],"b")
    1
    >>> binary_search(["a","b"],"c")
    -1
    >>> binary_search(["a","b"],None)
    -1

    :param list:
    :param element:
    :return: index
    """
    checklist = []
    index = 0
    for i in list:
        if(i not in checklist):
            checklist.append(i)
    for j in sorted(checklist):
        index +=1
        if(element == j):
            return index-1
    return -1