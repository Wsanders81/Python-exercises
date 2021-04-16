def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_lower =  phrase.lower().split()
    completed_string = ""
    for word in phrase_lower:
        completed_string = completed_string+ str(word).capitalize()+ " "  
    return completed_string