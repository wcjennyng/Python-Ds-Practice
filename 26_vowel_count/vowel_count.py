def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    dict = {}
    vowels = {'a','e','i','o','u'}
    for letter in phrase.lower():
        if letter in vowels:
            dict[letter] = dict.get(letter,0) + 1
    return dict