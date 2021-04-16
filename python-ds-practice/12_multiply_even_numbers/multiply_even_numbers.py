def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    # read the directions wrong but I was still happy I got this haha
    # return [num * 2 if num % 2 == 0 else num for num in nums]
    sum = 1
    for num in nums: 
        if num % 2 == 0: 
            sum = sum * num
    return sum
        