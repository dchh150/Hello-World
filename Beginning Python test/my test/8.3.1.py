try:
    1/0
except ZeroDivisionError:
    raise ValueError #from None

from warnings import warn
warn('fsa')
