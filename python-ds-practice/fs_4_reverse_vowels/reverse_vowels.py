def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    chars = list(s)
    
    idx = []
    vowels_list = []
    vowels = "aeiou"
    for i in range(len(chars)): 
        if chars[i].lower() in vowels: 
            vowels_list.append(chars[i])
            idx.append(i)
    new_vowels_list = vowels_list[::-1]
    output = []
    ind = 0
    for i in range(len(chars)): 
        
        if i in idx: 
            output.append(new_vowels_list[ind])
            ind += 1
        else: 
            output.append(chars[i])
    reversed_string = ""
    return reversed_string.join(output)

