def ana(word):
    if word[0] in 'aeiou':
        return 'an ' + word
    else:
        return 'a ' + word
