def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_to_swap = to_swap.lower()
    new_phrase = ""
    for ltr in phrase:
        if ltr.lower() == new_to_swap:
            ltr = ltr.swapcase()
        new_phrase += ltr
    return new_phrase
