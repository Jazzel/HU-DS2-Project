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
        # a, b = self._hasLeft(index), self._hasRight(index)
        # if a and b:
        #     small_child = min(self._left(index), self._right(index))
        # elif a:
        #     small_child = self._left(index)
        # elif b:
        #     small_child = self._right(index)
        # else:
        #     return
        
        if self._hasLeft(index):
            left = self._left(index)
            small_child = left # although right may be smaller
            if self._hasRight(index):
                right = self._right(index)
                if self._array[right] < self._array[left]:
                    small_child = right

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
class Pagoda():
    # Constructor of this class
    def __init__(self):
        # Initializing the root in the Pagoda as None
        self.root = None
    
    def isEmpty(self):
        # Returns true if root is equal to null
        # else returns false
        return self.root is None
    
    def clear(self):
        # Clears or Empties the entire Pagoda
        self.root = None
    
    def add(self, data):
        if self.root == None:
            self.root = Pagoda_Node(data)
        else:
            self._add(self.root, Pagoda_Node(data))
    
            
    # def traverse(self, root):
    #     if root == None:
    #         return
    #     print(root.data, end=' ')
    #     self.traverse(root.left)
    #     self.traverse(root.right)

    def traverse(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        if root.left is not None:
            self.traverse(root.left)
        if root.right is not None:
            self.traverse(root.right)

    
