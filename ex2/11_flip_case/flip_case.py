def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase = [letter for letter in phrase]
    print(phrase)
    new_phrase = []
    for letter in phrase:
        if to_swap == letter:
            letter = letter.swapcase()
            new_phrase.append(letter)
        elif to_swap.upper() == letter:
            letter = letter.swapcase()
            new_phrase.append(letter)
        elif to_swap.lower() == letter:
            letter = letter.swapcase()
            new_phrase.append(letter)
        else:
            new_phrase.append(letter)
    return(''.join(new_phrase))
