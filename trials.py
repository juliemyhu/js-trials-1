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
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
