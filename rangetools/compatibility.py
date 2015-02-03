
# ----------------------------------------------------------------------------

__all__ = [
    'built_in_range',
]

# ----------------------------------------------------------------------------

try:
    built_in_rnage = xrange
except NameError:
    built_in_range = range

