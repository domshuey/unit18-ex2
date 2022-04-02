def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_list = []
    for char in phrase:
        phrase_list.append(char)
    phrase_list.reverse()
    return(''.join(phrase_list))

