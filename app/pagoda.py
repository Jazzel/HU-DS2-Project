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
        '''
        root: if r is root, d(r) points to the bottom of right branch and g(r) points to the bottom of the 
        left branch

        left-son: if k is left son in tree T, g(k) points to the father of k and d(k) points to the bottom of
        the right branch starting at k.
        
        right-son: if k is right son in tree T, d(k) points to father of k and g(k) points  to the bottom of
        left branch starting at k.
        '''
        # Node stores the value as data
        self.data = val
        # Left pointer is initially set as itself
        self.d = None
        # Right pointer is initially set as itself
        self.g = None
    
    def get_data(self):
        return self.data

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
            node = Pagoda_Node(data)
            self.root = self.merge(self.root, node)
    
            
    def merge(self, root1, root2, res=None):
        # trivial cases
        if root2 is None and root1 is None:
            return res
        # if root1 is None or root2 is None:
        #     if root2 is None:
        #         root2,root1 = root1,root2
        if root1 == None:
            if root2.d is None:
                temp = root2
                root2 = None
            else:
                temp = root2.d
                if root2.d == None:
                    temp = root2
                    root2 = None
                elif temp.d == root2:
                    root2.d = None
                else:
                    root2.d = temp.d
            temp.d = res
            res = temp
            return self.merge(root1, root2, res)

        if root2 == None:    
            if root1.g is None:
                temp = root1
                root1 = None
            else:
                temp = root1.g
                if root1.g == None:
                    temp = root1
                    root1 = None
                elif temp.g == root1:
                    root1.g = None
                else:
                    root1.g = temp.g
            temp.g = res
            res = temp
            return self.merge(root1, root2, res)


        # merge bottom of right branch of root1 with bottom of left branch of root2
        bot_r_root1 = root1.d # bottom of right branch of root1
        if bot_r_root1 == None:
            bot_r_root1 = root1
        
        bot_l_root2 = root2.g # bottom of left branch of root2
        if bot_l_root2 == None:
            bot_l_root2 = root2

        # we know that bot_r_root1 is right son (bec it is bottom of right branch), 
        # there fore self.d points to father and self.g points to bottom of left branch
        # inverse is true for bot_l_root2

        # if root1's bottom of right branch is greater than root2's bottom of left branch,
        # then we merge root1's bottom of right branch with res
        if (bot_r_root1.get_data() >= bot_l_root2.get_data()):
            if(root1.get_data() == bot_r_root1.get_data()):
                root1 = None
            else:
                # root1's new right bottom (root.d) is previous right bottom k's father, k.d
                root1.d = bot_r_root1.d
                if root1.d != None and root1.get_data() == root1.d.get_data():
                    root1.d = None

            # add res as the right branch of bot_r_root1
            bot_r_root1.d = res
            # new res = bot_r_root1
            res = bot_r_root1
        else:
            if root2.get_data() == bot_l_root2.get_data():
                root2 = None
            else:
                # root2's new left bottom (root.g) is previous left bottom k's father, k.g
                root2.g = bot_l_root2.g
                if root2.g != None and root2.get_data() == root2.g.get_data():
                    root2.g = None
            # add res as the left branch of bot_l_root2
            bot_l_root2.g = res
            res = bot_l_root2
        return self.merge(root1, root2, res)

    def remove_min(self):
        if self.isEmpty():
            raise ValueError("Queue is empty")
        temp = self.root
        # min at root, swap it with leaf
        self.root = self.merge(self.root.d, self.root.g)
        return temp.get_data()

