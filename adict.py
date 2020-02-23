"""
-----------------------------
| o                       o |
|   Axel Ország-Krisz Dr.   |
| o                       o |
-----------------------------

AttributedDict
==============

Simple class to store and get data dictionary-like and object-like as well.
It has basic deffence against ovveriding mandatory attributes inherited from dict.

Copyright Axel Ország-Krisz Dr. 2020
Distributed under the Boost Software License, Version 1.0.
See accompanying file LICENSE or a copy at https://www.boost.org/LICENSE_1_0.txt
"""


class AttributedDict(dict):
    """
    AttributedDict
    --------------
    This class handles data dicitionary-like and object-like at the same time.
    This class inherits all methods and attributes from the dict superclass.
    """



    def __init__(self, *args, **kwargs):
        """
        Initializes the instance
        ------------------------
        @Params: anything   [optional] Any parameter is accepted without any
                            check since everything is forwarded to superclass
                            to ensure the most possible functionality.
        """

        super(self.__class__, self).__init__(*args, **kwargs)



    def __delattr__(self, key):
        """
        Deletes an attribute
        --------------------
        @Params: key    (string)    Key to delete.
        @Raises: AttributeError     If key is a reserved keyword.
                 AttributeError     If key doesn't exist.
        """

        if self.is_reserved(key):
            raise AttributeError('AttributedDict: tried to delete a reserved attribute "{}".'.format(key))
        elif key in self:
            del self[key]
        else:
            raise AttributeError('AttributedDict: tried to delete non-existing key "{}".'.format(key))



    def __getattr__(self, key):
        """
        Gets an attribute
        -----------------
        @Params: key    (string)    Key to get.
        @Return: (anything)         Corresponding value of the key.
        @Raises: AttributeError     If key doesn't exist.
        """

        if key in self:
            return self[key]
        else:
            raise AttributeError('AttributedDict: tried to get non-existing key "{}".'.format(key))



    def __setattr__(self, key, value):
        """
        Sets an attribute
        -----------------
        @Params: key    (string)    Key to set.
                 value  (anything)  Value to set.
        @Raises: AttributeError     If key is a reserved keyword.
        """

        if self.is_reserved(key):
            raise AttributeError('AttributedDict: tried to set a reserved attribute "{}".'.format(key))
        else:
            self[key] = value



    @classmethod
    def is_reserved(cls, key):
        """
        Checks if key is reserved
        -------------------------
        @Params: key    (string)    Key to set.
        @Return: (boolean)          True if key is reserved, else False.
        """

        return key in ['__class__', '__contains__', '__delattr__', '__delitem__',
                       '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
                       '__getattribute__', '__getitem__', '__gt__', '__hash__',
                       '__init__', '__init_subclass__', '__iter__', '__le__',
                       '__len__', '__lt__', '__ne__', '__new__', '__reduce__',
                       '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
                       '__sizeof__', '__str__', '__subclasshook__', 'clear',
                       'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
                       'popitem', 'setdefault', 'update', 'values']
