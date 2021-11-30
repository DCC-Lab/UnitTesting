from exceptions import EmptyStackException
from stack import Stack
import unittest


class TestStack1(unittest.TestCase):
    """ These tests do not follow all good practices, but are left like
    this to act as a simple example for new-comers.

    Each test has to include the 3 parts: Arrange, Act, Assert.
    These 3 parts are also written in the method name (here using one convention):
      `given<CONTEXT>_when<ACTION>_should<BEHAVIOUR>`.

    For a test to be seen in Python, its name has to start with the word `test`. """

    def testGivenANewStack_shouldBeEmpty(self):
        """ First test to write. We want to document the initial condition (no action taken). """
        stack = Stack()
        self.assertTrue(stack.isEmpty)

    def testGivenANewStack_whenPush_shouldAddElement(self):
        """ From now on we want to document the expected behaviour of the class, one step at a time.
        Make sure not to look inside the class, but instead keep it as a black box so your tests are less fragile.
        You can visually hide the implementation details of the class to help with that.

        Typical error:
            stack = Stack()
            stack.push(5)
            self.assertEqual(5, stack.elements[0]) -> BAD! accessing implementation details
         """
        stack = Stack()
        stack.push(5)
        self.assertFalse(stack.isEmpty)

    def testGivenAnElement_whenPop_shouldRemoveElement(self):
        """ The expected outcome is NOT that the stack should be empty again.
        The behaviour we expect is that the element will be removed from the stack.
        The check to `isEmpty` is just a way to test this behaviour. """
        stack = Stack()
        stack.push(5)
        stack.pop()
        self.assertTrue(stack.isEmpty)

    def testGivenAnElement_whenPop_shouldReturnElement(self):
        """ Go through one context and action at a time and make sure
        that all behaviours are documented. In this case, for the same
        context and action, we have another behaviour to document. """
        stack = Stack()
        stack.push(5)
        elementReturned = stack.pop()
        self.assertEqual(5, elementReturned)

    def testGivenMultipleElements_whenPop_shouldReturnInReversedOrder(self):
        """ In order to verify this behaviour in Python we will
        need to do 2 physical assertions, but this is still
        considered a single logical assertion.. """
        stack = Stack()
        stack.push(5)
        stack.push(25)

        firstElementReturned = stack.pop()
        secondElementReturned = stack.pop()

        self.assertEqual(25, firstElementReturned)
        self.assertEqual(5, secondElementReturned)

    def testGivenAnEmptyStack_whenPop_shouldRaiseException(self):
        """ Asserting that an exception is raised requires a special syntax. """
        stack = Stack()
        with self.assertRaises(EmptyStackException):
            stack.pop()


if __name__ == '__main__':
    unittest.main()
