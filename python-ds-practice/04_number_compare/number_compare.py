def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    # numbers = [ab]
    # return ['Numbers are equal' if a == b else 'Second is greater' if a < b else 'First is greater'  for num in numbers]
    if a == b:
        return "Numbers are equal"
    elif a < b: 
        return "Second is greater"
    else: 
        return "First is greater"