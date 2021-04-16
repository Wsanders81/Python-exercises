def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    vowel_dict = {}
    phrase_lower = phrase.lower()
    for ltr in phrase_lower:
        if ltr in vowels:
            vowel_dict[ltr] = phrase_lower.count(ltr)
    return vowel_dict