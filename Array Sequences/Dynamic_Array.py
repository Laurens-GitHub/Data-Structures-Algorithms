"""This module makes a dynamic array class without the use of a built-in list class"""

import ctypes
import sys
#We're using the ctypes library to make a raw array

class DynamicArray(object):
    """A dynamic list class"""

    def __init__(self):
        """initiates the list"""
        self.element_count = 0 # the initial list is empty
        self.capacity = 1 # by default the list can only accept 1 element
        self.a_list = self.make_array(self.capacity)

    def __len__(self):
        """returns the number of elements stored in the list"""
        return self.element_count

    def __getitem__(self,k):
        """return the item at the given index, k"""
        if not 0 <= k < self.element_count: # if the index passed isn't between 0 and the length of the array
            return IndexError("K is out of bounds!") # we need to return an error

        return self.a_list[k]

    def append(self,element):
        """add an element to the end of the list"""
        # if our list is at capacity, we need to make it larger before we add another element

        if self.element_count == self.capacity:
            self._resize(2*self.capacity) # double the capacity

        self.a_list[self.element_count] = element
        self.element_count += 1

    def _resize(self, new_capacity):
        """resize the initial array to the new capacity"""
        b_list = self.make_array(new_capacity) # <~ new, bigger array

        for k in range(self.element_count): # reference all existing values from the initial array into the new one
            b_list[k] = self.a_list[k]

        self.a_list = b_list # make the initial array into the bigger array
        self.capacity = new_capacity # set our new bigger capacity

    def make_array(self, new_capacity):
        """return our array object"""
        return (new_capacity * ctypes.py_object)()

arr = DynamicArray()

for i in range(10):
    print(len(arr), sys.getsizeof(arr))
    arr.append(i)
