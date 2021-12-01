# Unit testing

## Exercise 1: The Stack

![image-20211130170910111](assets/stack_representation.jpg)

This repository provides a simple implementation of a stack in Python inside `stack.py`. This stack offers the following behavior: 

- **isEmpty** – Returns whether the stack is empty.
- **push(element)** – Inserts the element at the top of the stack.
- **pop()** – Deletes and returns the topmost element of the stack. Raises an `EmptyStackException` if trying to pop an empty stack. 

The goal of this exercise is to **create a test file that documents this behavior**. 



### Solution

You will find a test file template inside `/solutions` as well as a few valid solutions to this exercise:

- `testStackDCC.py` : solution written during the DCC-Lab workshop.
- `testStack1.py` : a reference solution including explanations for some part of the thought-process.   
- `testStack2.py` : a slightly improved version of `testStack1.py` that uses constants and a setup method. 