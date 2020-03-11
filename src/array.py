class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

    def insert(self, index, value):

        self.storage[index] = value

        for idx in range(self.count, index, -1):
            self.storage[idx] = self.storage[idx - 1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        if self.count == self.capacity:
            print("Array is full!")
            return
        self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        # double the capacity
        self.capacity = self.capacity * 2
        # make a new array twice the size of the old one
        new_arr = [None] * self.capacity

        # copy everything over
        for i in range(self.count):
            new_arr[i] = self.storage[i]

        self.storage = new_arr

# O(n^2)


def add_to_front(n):
    x = []
    for i in range(n):
        x.insert(i, n-1)
    return x

# O(n)


def add_to_back(n):
    x = []
    for i in range(n):
        x.append(i)
    return x

# O(n) but it should be faster because we dont have to resize it again


def preallocate(n):
    x = [None] * n
    for i in range(n):
        x[i] = i
    return x
