def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
   
    is_list = 0
    for item in lst: 
        if isinstance(item,list):
            is_list += 1
    
    return is_list == len(lst)