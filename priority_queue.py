from abc import ABC, abstractmethod
class PriorityQueue(ABC):
    """
    Abstract Base class for Priority Queue implementations
    Defines the primitive methods that every implementation should provide
    """

    @abstractmethod
    def add(self, key, value) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def min(self) -> tuple:
        raise NotImplementedError
    
    @abstractmethod
    def remove_min(self) -> tuple:
        raise NotImplementedError
    
    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError
    
    def isEmpty(self):
        return len(self) == 0
    


class ArrayHeapPriorityQueue(PriorityQueue):
    '''
    Implementation of Priority Queue using array-based heap.
    
    len(P), P.is empty() ---> O(1)
    P.min() ----------------> O(1)
    P.add() ----------------> O(log n)∗
    P.remove_min() ---------> O(log n)∗
    '''

    def _parent(self, index):
        return (index - 1)//2

    def _left(self,index):
        return 2*index + 1
    
    def _right(self,index):
        return 2*index + 2

    def _hasLeft(self, index):
        return self._left(index) < len(self._array)

    def _hasRight(self, index):
        return self._right(index) < len(self._array)
    
    def _swapNodes(self, i, j):
        self._array[i], self._array[j] = self._array[j], self._array[i]

    def _upHeap(self, index):
        parent = self._parent(index)
        if index > 0 and self._array[index] < self._array[parent]:
            self._swapNodes(index, parent)
            self._upHeap(parent)

    def _downHeap(self, index):
        a, b = self._hasLeft(index), self._hasRight(index)
        if a and b:
            small_child = min(self._left(index), self._right(index))
        elif a:
            small_child = self._left(index)
        elif b:
            small_child = self._right(index)
        else:
            return
        
        if self._array[small_child] < self._array[index]:
            self._swapNodes(index, small_child)
            self._downHeap(small_child)

    def __init__(self) -> None:
        self._array = []

    def __len__(self) -> int:
        return len(self._array)

    def add(self, node):
        self._array.append(node)
        self._upHeap(len(self._array) - 1)

    def min(self) -> tuple:
        if self.isEmpty():
            raise ValueError("Queue is empty")
        return self._array[0]

    def remove_min(self) -> tuple:
        if self.isEmpty():
            raise ValueError("Queue is empty")
        # min at root, swap it with leaf
        self._swapNodes(0, len(self._array) - 1)
        node = self._array.pop()
        self._downHeap(0)
        return node
        


# Class for creating a single node
class Pagoda_Node:
    def __init__(self, val):
        # Node stores the value as data
        self.data = val
        # Left pointer is initially set as itself
        self.left = self
        # Right pointer is initially set as itself
        self.right = self

# Helper class
# Pagoda class
class Pagoda(PriorityQueue):
    # Constructor of this class
    def __init__(self):
        # Initializing the root in the Pagoda as None
        self.root = None
    
    # Method 1
    # To check if Pagoda is empty
    def isEmpty(self):
        # Returns true if root is equal to null
        # else returns false
        return self.root is None
    
    # Method 2
    # To clear the entire Pagoda
    def clear(self):
        # Clears or Empties the entire Pagoda
        self.root = None
    
    # Method 3
    # To insert node into the Pagoda
    def add(self, val):
        # Creates a new node with data as val
        node = Pagoda_Node(val)
        # Inserts into Pagoda
        self.root = self._insert(node, self.root)

    def _insert(self, node, queue):
        # Initially the new node has no left child
        # so the left pointer points to itself
        node.left = node
        # Initially the new node has no right child
        # so the right pointer points to itself
        node.right = node
        # Calling merge to attach new node to Pagoda
        return self._merge(queue, node)

    # Method 4
    # To merge new node to Pagoda
    # New node is inserted as a leaf node
    # and to maintain the heap property
    # if the new node is greater than its parent
    # both nodes are swapped and this continues till
    # all parents are greater than its children
    def _merge(self, root, newnode):
        if root is None:
            # If root is null, after merge - only newnode
            return newnode
        elif newnode is None:
            # If newnode is null, after merge - only root
            return root
        else:
            # Bottom of root's rightmost edge
            botroot = root.right
            root.right = None
            # bottom of newnode's leftmost edge - mostly
            # itself
            botnew = newnode.left
            newnode.left = None
            r = None
            # Iterating via loop for merging
            while botroot is not None and botnew is not None:
                # Comparing parent and child
                if botroot.data < botnew.data:
                    temp = botroot.right
                    if r is None:
                        botroot.right = botroot
                    else:
                        botroot.right = r.right
                        r.right = botroot
                    r = botroot
                    botroot = temp
                else:
                    # Comparing parent and child
                    temp = botnew.left
                    if r is None:
                        botnew.left = botnew
                    else:
                        # Swapping of child and parent
                        botnew.left = r.left
                        r.left = botnew
                    r = botnew
                    botnew = temp
            # Merging stops after either
            # botnew or botroot becomes null
            # Condition check when node(botnew) is null
            if botnew is None:
                root.right = r.right
                r.right = botroot
                return root

    