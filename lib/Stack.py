class Stack:

    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
            return True  # Return True to indicate successful push
        else:
            return False  # Return False to indicate stack is full

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) == self.limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i
        return -1


# Test cases for the Stack class
def test_search():
    '''Test Stack search() method. How far is the element in the stack? '''
    stk = Stack([5, 6, 7, 8, 9, 10])

    assert stk.search(5) == 1  # 5 is one element away from the top of the stack
    assert stk.search(9) == 4  # 9 is four elements away from the top of the stack
    assert stk.search(11) == -1  # 11 is not in the stack, so it should return -1


def test_push_pop():
    stk = Stack()
    stk.push(1)
    assert stk.pop() == 1


def test_peek():
    stk = Stack()
    stk.push(1)
    assert stk.peek() == 1


def test_is_empty():
    stk = Stack()
    assert stk.isEmpty() == True


def test_size():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    assert stk.size() == 2


def test_full():
    stk = Stack(2)
    stk.push(1)
    stk.push(2)
    assert stk.full() == True


def test_push_full():
    stk = Stack(2)
    assert stk.push(1) == True
    assert stk.push(2) == True
    assert stk.push(3) == False  # The stack is full, should return False


def test_pop_empty():
    stk = Stack()
    assert stk.pop() is None  # The stack is empty, should return None


def test_peek_empty():
    stk = Stack()
    assert stk.peek() is None  # The stack is empty, should return None


def test_search_empty():
    stk = Stack()
    assert stk.search(5) == -1  # The stack is empty, should return -1


if __name__ == "__main__":
    test_search()
    test_push_pop()
    test_peek()
    test_is_empty()
    test_size()
    test_full()
    test_push_full()
    test_pop_empty()
    test_peek_empty()
    test_search_empty()
    print("All tests passed!")
