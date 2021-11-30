import unittest

from exceptions import EmptyStackException
from stack import Stack


class TestStack(unittest.TestCase):
    AN_ELEMENT = 2012
    LAST_ELEMENT_PUSHED = 51
    FIRST_ELEMENT_PUSHED = 915

    def testCreateStack(self):
        stack = Stack()

        self.assertIsNotNone(stack)

    def testANewStackIsEmpty(self):
        stack = Stack()

        self.assertTrue(stack.isEmpty)

    def testWhenPushAnElement_shouldAddTheElement(self):
        stack = Stack()
        
        stack.push(self.AN_ELEMENT)

        self.assertFalse(stack.isEmpty)

    def testGivenOneElement_whenPop_shouldReturnElement(self):
        stack = Stack()
        stack.push(self.LAST_ELEMENT_PUSHED)

        elementReturned = stack.pop()

        self.assertEqual(self.LAST_ELEMENT_PUSHED, elementReturned)

    def testGivenOneElement_whenPop_shouldRemoveElement(self):
        stack = Stack()
        stack.push(self.AN_ELEMENT)
        
        stack.pop()
        
        self.assertTrue(stack.isEmpty)

    def testGivenMultipleElements_whenPop_shouldReturnLastElementPushed(self):
        stack = Stack()
        stack.push(self.AN_ELEMENT)
        stack.push(self.LAST_ELEMENT_PUSHED)

        elementReturned = stack.pop()
        
        self.assertNotEqual(self.AN_ELEMENT, elementReturned)
        self.assertEqual(self.LAST_ELEMENT_PUSHED, elementReturned)

    def testGivenMultipleElements_whenPop_shouldReturnElementsInReversedOrder(self):
        stack = Stack()
        stack.push(self.FIRST_ELEMENT_PUSHED)
        stack.push(self.LAST_ELEMENT_PUSHED)

        firstElementReturned = stack.pop()
        secondElementReturned = stack.pop()
        
        self.assertEqual(self.LAST_ELEMENT_PUSHED, firstElementReturned)
        self.assertEqual(self.FIRST_ELEMENT_PUSHED, secondElementReturned)

    def testAnEmptyStack_whenPop_shouldRaiseAnEmptyStackException(self):
        stack = Stack()

        with self.assertRaises(EmptyStackException):
            stack.pop()


if __name__ == '__main__':
    unittest.main()
