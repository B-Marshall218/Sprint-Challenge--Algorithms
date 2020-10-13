'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:
        return 0
    # Grab the first two letters in word
    slice = word[:2]
    # Do they equal "th"
    if slice == "th":
        return 1 + count_th(word[1:])
    # If so return 1 plus a recrusive call passing
    # in everything but the frist letter in word
    print(word)
    # If the letters dont = th drop the first letter from word
    #  and make a recursive call to start over
    return count_th(word[1:])


# TBC
