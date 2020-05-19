"""Python functions for JavaScript Trials 1."""


def output_all_items(items):

    """ 
    Ex:
    >>> output_all_items([1, 'hello', True])
    1
    hello
    True

    """
    for item in items:
        print(item)

def get_all_evens(nums):
    """
    Ex:
    >>> get_all_evens([7, 8, 10, 1, 2, 2])
    [8, 2, 2]


    """
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    """
    Ex:
    >>> get_odd_indices([1, 'hello', True, 500])
    ['hello', 500]

    """
    result = []
    for idx, i in enumerate(items):
        if idx % 2 != 0:
            result.append(i)

    # for i in range(len(items)):
    #     if i % 2 !=0:
    #         result.append(i)

    return result

def print_as_numbered_list(items):
    """
    Ex:
    >>> print_as_numbered_list([1, 'hello', True])
    1. 1
    2. hello
    3. True

    """
    i = 1
    for item in items:
        print (f'{i}. {item}')
        i += 1 

def get_range(start, stop):
    """
    Ex: 
    >>> get_range(0, 5)
    [0, 1, 2, 3, 4]

    """
    nums = []
    for num in range (start, stop):
        nums.append(num)
    return nums

def censor_vowels(word):
    """
    Ex.
    >>> censor_vowels('hello world')
    'h*ell*o w*orld'

    """

    chars = []
    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        chars.append(letter)

    return "".join(chars)

def snake_to_camel(string):

    """
    Ex.
    >>> snake_to_camel('hello_world')
    'HelloWorld'
    """
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return "".join(camel_case)


def longest_word_length(words):

    """
    Ex.
    >>> longest_word_length(['hello','world'])
    5
    >>> longest_word_length(['jellyfish', 'zebra'])
    9

    """
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

def truncate(string):

    """
    Ex.
    >>> truncate('aaaabbbbcccca')
    'abca'
    >>> truncate('hi***!!!! wooow')
    'hi*! wow'

    """

    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return "".join(result) 


def has_balanced_parens(string):


    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

        if parens < 0:
            return False

    return parens == 0;


def compress(string):
    """
    Ex:
    >>> compress('aabbaabb')
    'a2b2a2b'
    >>> compress('abc')
    'abc'
    >>> compress('Hello, world! Cows go moooo...')
    'Hel2o, world! Cows go mo4.3'

    """
    compressed = []
    curr_char = ''
    char_count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0
        char_count += 1

    compressed.append(curr_char)
    if char_count > 2:
        compressed.append(str(char_count))

    return "".join(compressed)
