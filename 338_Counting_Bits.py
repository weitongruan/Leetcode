def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """

    """ First idea: results in Memory Limit Exceeded
    """
    counter = 0
    baselist = [0]
    previous_list = baselist
    update_list = baselist
    while 2 ^ counter <= num:
        counter += 1
        previous_list = update_list
        update_list = previous_list + [i + 1 for i in previous_list]

    if counter:
        return update_list + [i + 1 for i in update_list[:num - 2 ^ (counter - 2)]]
    else:
        return [0] if num == 0 else [0, 1]

    """ A better implementation online
    """

    baselist = [0]
    if num > 0:
        while len(baselist) < num + 1:
            baselist += [i + 1 for i in baselist]

    return baselist[:num + 1]

    """ To use lambda operator and map(): This is shorter but actually slower!
    """
    baselist = [0, 1]
    while len(baselist) < num + 1:
        baselist += map(lambda x : x+1, baselist)
    return baselist[:num + 1]

    """ How about this:
    """
    baselist = [0, 1]
    while len(baselist) < num + 1:
        baselist += [i + 1 for i in baselist]
    return baselist[:num + 1]
