# Description: You are tasked with creating a Rectangle class with the following requirements:

# An instance of the Rectangle class requires length:int and width:int to be initialized.
# We can iterate over an instance of the Rectangle class 
# When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}


# Solution :

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Creating a list of length and width as dictionaries
        dimensions = [{'length': self.length}, {'width': self.width}]
        # Returning an iterator for the list
        return iter(dimensions)

# Example usage
rectangle = Rectangle(10, 5)

# Iterating over the rectangle instance
for dimension in rectangle:
    print(dimension)
