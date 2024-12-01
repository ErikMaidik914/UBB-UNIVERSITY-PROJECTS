import copy


class Node:
    """
    Represents a node in the linked list used to handle hash collisions.

    Attributes:
        key: The key to be stored (value in this case).
        value: The position (bucket index, relative position) where the key is stored.
        next: Pointer to the next node in the linked list.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A simple hash table with linked-list chaining for collision handling.

    Attributes:
        capacity: The initial size of the bucket list (defaults to 2).
        size: The current number of elements in the table.
        buckets: A list of linked lists representing the hash table.
    """

    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity

    def _hash(self, value):
        """
        Computes the hash for a given value.

        Args:
            value: The value to hash.

        Returns:
            The bucket index where the value should be stored.
        """
        return abs(hash(value) % self.capacity)

    def add(self, value):
        """
        Adds a value to the hash table. Resizes and rehashes if load factor > 0.5.

        Args:
            value: The value to be added to the table.
        """
        if self.size and (self.capacity // self.size < 2):
            self.__resize_and_rehash()

        pos = self._hash(value)
        elem = self.buckets[pos]

        if elem is None:
            self.buckets[pos] = Node(value, (pos, 0))
        else:
            pos_relative = 1
            while elem.next is not None:
                pos_relative += 1
                elem = elem.next
            elem.next = Node(value, (pos, pos_relative))

        self.size += 1

    def get(self, value):
        """
        Retrieves the position of the value in the table.

        Args:
            value: The value to be looked up.

        Returns:
            The position (bucket index, relative position) if found, else None.
        """
        elem = self.buckets[self._hash(value)]
        while elem is not None:
            if elem.key == value:
                return elem.value
            elem = elem.next
        return None

    def __resize_and_rehash(self):
        """
        Doubles the capacity of the table and rehashes all existing values.
        """
        self.capacity *= 2
        old_buckets = copy.deepcopy(self.buckets)
        self.buckets = [None] * self.capacity
        self.size = 0

        for elem in old_buckets:
            while elem is not None:
                self.add(elem.key)
                elem = elem.next