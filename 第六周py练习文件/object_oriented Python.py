#
l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
print(type(l))
print(type(s))
print(type(d))

#
class NewList():
    pass

#
class NewList(DQ):
    pass

newlist_1 = NewList()
print(type(newlist_1))

#
class NewList(DQ):
    def first_method():
        return "This is my first method"

newlist = NewList()

#
class NewList(DQ):
    def first_method(self):
        return "This is my first method"

newlist = NewList()
result = newlist.first_method()

#
class NewList(DQ):
    def return_list(self, input_list):
        return input_list

newlist = NewList()
result = newlist.return_list([1, 2, 3])

#
class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state

my_list = NewList([1, 2, 3, 4, 5])
print(my_list.data)

#
class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
    
    def append(self, new_item):
        """
        Append `new_item` to the NewList
        """
        self.data = self.data + [new_item]

my_list = NewList([1, 2, 3, 4, 5])
print(my_list.data)
my_list.append(6)
print(my_list.data)

#
class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()
    
    def calc_length(self):
        """
        A helper function to calculate the .length
        attribute.
        """
        length = 0
        for item in self.data:
            length += 1
        self.length = length
    
    def append(self, new_item):
        """
        Append `new_item` to the NewList
        """
        self.data = self.data + [new_item]
        self.calc_length()

fibonacci = NewList([1, 1, 2, 3, 5])
print(fibonacci.length)

fibonacci.append(8)
print(fibonacci.length)




