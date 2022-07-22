import collections.abc

"""
sources:
    https://docs.python.org/3/library/collections.abc.html
    https://digitology.tech/docs/python_3/library/collections.abc.html
"""

print(*dir(collections.abc.Sequence), sep='\n')
print('\n', '-' * 50, '\n')
print(*dir(collections.abc.MutableSequence), sep='\n')