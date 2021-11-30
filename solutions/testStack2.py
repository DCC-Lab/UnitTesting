from exceptions import EmptyStackException
from stack import Stack
import unittest


class TestStack2(unittest.TestCase):
    """ Don't distract the reader with dummy values.
    Extract to a constant with a meaningful name."""
    AN_ELEMENT = 1531
    FIRST_ELEMENT_PUSHED = 71
    LAST_ELEMENT_PUSHED = 925

    def setUp(self):
        """ This magic method name will trigger the module to run it
        before every test method. If we could rename it, it would be called
        `givenANewStack`. This is usually written after a few tests when
        the initial conditions is being repeated. """
        self.stack = Stack()

    def testShouldBeEmpty(self):
        self.assertTrue(self.stack.isEmpty)

    def testWhenPush_shouldAddElement(self):
        self.stack.push(self.AN_ELEMENT)
        self.assertFalse(self.stack.isEmpty)

    def testGivenAnElement_whenPop_shouldRemoveElement(self):
        self.stack.push(self.AN_ELEMENT)
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty)

    def testGivenAnElement_whenPop_shouldReturnElement(self):
        """ Use constants with meaningful names that not only fits the behaviour,
        but also reads like a story: Once upon a time there was a Stack..."""
        self.stack.push(self.LAST_ELEMENT_PUSHED)
        elementReturned = self.stack.pop()
        self.assertEqual(self.LAST_ELEMENT_PUSHED, elementReturned)

    def testGivenMultipleElements_whenPop_shouldReturnInReversedOrder(self):
        self.stack.push(self.FIRST_ELEMENT_PUSHED)
        self.stack.push(self.LAST_ELEMENT_PUSHED)

        firstElementReturned = self.stack.pop()
        secondElementReturned = self.stack.pop()

        self.assertEqual(self.LAST_ELEMENT_PUSHED, firstElementReturned)
        self.assertEqual(self.FIRST_ELEMENT_PUSHED, secondElementReturned)

    def testGivenNoElements_whenPop_shouldRaiseException(self):
        with self.assertRaises(EmptyStackException):
            self.stack.pop()


if __name__ == '__main__':
    unittest.main()
