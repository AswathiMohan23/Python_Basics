def fun(alphabets):
    letters = ['a', 'e', 'i', 'o', 'u']
    if alphabets in letters:
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'i', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for i in filtered:
    print(i)