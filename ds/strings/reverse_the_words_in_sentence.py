def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here
    reversed_string = ''
    for i in range(len(our_string), 0, -1):
        reversed_string = reversed_string + our_string[i-1]
    return reversed_string


def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here
    result = ''
    while True:
        str1, sep, our_string = our_string.partition(' ')
        reversed_word = string_reverser(str1)
        result = result + ' ' + reversed_word
        if sep == '' and our_string == '':
            break
    result = result.strip()
    return result


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
