from src.stack.stinlist import Stack
import pytest
def test_stack_initialization():
    stack = Stack()
    assert stack.is_empty() == True
    assert stack.__len__() == 0

def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.is_empty() == False
    assert stack.__len__() == 1

def test_stack_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.__len__() == 3
    assert stack.is_empty() == False

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True

def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError, match="Stack is empty"):
        stack.pop()

def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.__len__() == 2  

def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError, match="Stack is empty"):
        stack.peek()

def test_stack_length():
    stack = Stack()
    assert stack.__len__() == 0
    stack.push(1)
    assert stack.__len__ ()== 1
    stack.push(2)
    assert stack.__len__ ()== 2
    stack.pop()
    assert stack.__len__() == 1

def test_stack_mixed_operations():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert stack.pop() == 20
    assert stack.peek() == 10
    stack.push(30)
    assert stack.pop() == 30
    assert stack.pop() == 10
    assert stack.is_empty() == True

