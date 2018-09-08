def count_unique(list):
    """Count the number of distinct elements in a list.

        The list can contain any kind of elements, including duplicates and nulls in any order.

        (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

        :param list:  list of elements to find distinct elements of
        :return: the number of distinct elements in list

        Examples:
        >>> count_unique(['a','b','b','b','a','c','c'])
        3
        >>> count_unique(['a','a','a','a'])
        1
        >>> count_unique([ ])
        0
        """
    newlist = []
    for i in list:
        if (i not in newlist):
            newlist.append(i)
    return len(newlist)


def binary_search(list,element):
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
