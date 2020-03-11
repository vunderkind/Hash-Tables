# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        hash = 5381
        for letter in key:
            hash = (hash * 33) + ord(letter)
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # print(hash)
        return hash

    def _hash_djb2(self, key):
        hash = 5381
        for letter in key:
            hash = (hash * 33) + ord(letter)
        return hash
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        if self.storage[self._hash_mod(key)] != None:
            current = self.storage[self._hash_mod(key)]
            while current:
                if current.key == key:
                    current.value = value
                    break
                if current.next != None:
                    current = current.next
                else:
                    break
            current.next = LinkedPair(key, value)
        else:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)
        '''
        Store the value with the given key.
        Fill this in.
        '''
        # pass

    def remove(self, key):
        # print("@@@@@@@@@@@")
        if self.storage[self._hash_mod(key)] != None:
            previous = None
            current = self.storage[self._hash_mod(key)]
            next = current.next
            while True:
                if current.key == key:

                    # If node is in the middle
                    if previous != None and next != None:
                        previous.next = next
                        break
                    # If Node is first and has one after
                    if previous == None and next != None:
                        self.storage[self._hash_mod(key)] = next
                        break
                    # If node is first and only Node
                    if previous == None and next == None:
                        self.storage[self._hash_mod(key)] = None
                        break
                    # If node is Last and has one before
                    if previous != None and next == None:
                        previous.next = None
                        break

                # If we don't see the key and there is another node to check, move temp nodes forward and repeat
                elif current.next != None:
                    previous = current
                    current = current.next
                    next = current.next

                # Couldn't find anything and no more nodes left
                else:
                    print('No such key!')
                    break

        else:
            print('No such key')

        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        pass

    def retrieve(self, key):

        if self.storage[self._hash_mod(key)] != None:
            current = self.storage[self._hash_mod(key)]
            while True:
                if current.key == key:
                    return current.value
                elif current.next != None:
                    current = current.next
                else:
                    return None

        else:
            return None

        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        pass

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        tempstorage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for node in tempstorage:
            if node != None:
                current = node
                while current:
                    self.insert(current.key, current.value)
                    current = current.next
        # pass


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
