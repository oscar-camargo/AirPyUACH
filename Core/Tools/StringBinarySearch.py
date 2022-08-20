def stringbinarysearch(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        middle = (start+end) // 2
        midpoint = lst[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle