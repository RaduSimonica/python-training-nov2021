# Import module
# import long_strings
#
#
# print(long_strings.get_longer_strings('ceva', 'altceva', 'încă ceva', n=5))

# Import certain name(s) from a module
# from long_strings import get_longer_strings as get_strings
# # from legb import VERSION, func
#
# print(get_strings('ceva', 'altceva', 'încă ceva', n=5))

# Import a package -- only __init__.py will be loaded
# import pypackage

# Import a module from a package
from pypackage import pymodule
pymodule.pyfunc('Ana')
