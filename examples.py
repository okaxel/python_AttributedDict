"""
-----------------------------
| o                       o |
|   Axel Ország-Krisz Dr.   |
| o                       o |
-----------------------------

AttributedDict - examples
=========================

This script demonstrates the usage of AttributedDict.

Copyright Axel Ország-Krisz Dr. 2020
Distributed under the Boost Software License, Version 1.0.
See accompanying file LICENSE or a copy at https://www.boost.org/LICENSE_1_0.txt
"""



from adict import AttributedDict



def main():

    # Ways of creating an AttributedDict is same as to create a dictionary
    # but you cannot use the curly brackets form.
    exampledict = AttributedDict()
    print('Empty dictionary:\n{}'.format(exampledict))
    # You can use a list for with nested tuples as keys and values.
    exampledict = AttributedDict([('firstkey', 'first value'),
                                  ('secondkey', 'second value'),
                                  ('thirdkey', 'third value')])
    print('Non-empty dictionary:\n{}'.format(exampledict))
    # Dict-style vs. object-style
    print('Dict-style first key:\nexampledict[\'firstkey\'] has a value of \'{}\''
          .format(exampledict['firstkey']))
    print('Object-style first key:\nexampledict.firstkey has a value of \'{}\''
          .format(exampledict.firstkey))
    # Some protection against mistakes
    # set
    try:
        exampledict.keys = ['newfirstkey', 'newsecondkey', 'newthirdkey']
        print('This success is not a succcess.')
    except AttributeError as attrerr:
        print('Keys is a protected attribute of dictionary so error is totally expected')
        print(attrerr)
    # del
    try:
        del exampledict.items
        print('This success is not a succcess.')
    except AttributeError as attrerr:
        print('Items is a protected attribute of dictionary so error is totally expected')
        print(attrerr)
    # It's time to finish now and it's your turn to use AttributedDict.
    print('Demonstration finished.')



if __name__ == '__main__':
    main()
else:
    print('This is a script not a module.')
