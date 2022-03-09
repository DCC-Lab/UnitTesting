from exceptions import EmptyStackException


class Stack:
    def __init__(self):
        self.elements = []

    @property
    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.isEmpty:
            raise EmptyStackException("Cannot pop an empty stack.")
        else:
            element = self.elements[-1]
            self.elements.remove(element)
            return element
