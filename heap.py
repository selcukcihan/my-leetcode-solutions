class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class MyHeap:
    def __init__(self):
        self.root = None
        self.next_candidates_parent = None

    def min(self):
        return self.root.value
    
    def remove_min(self):
        pass

    def _swap(self, child, parent):
        temp = parent.value
        parent.value = child.value
        child.value = temp

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            if self.next_candidates_parent is None:
                self.next_candidates_parent = node
        else:
            if self.next_candidates_parent.left:
                self.next_candidates_parent.right = node
            else:
                self.next_candidates_parent.left = node
            node.parent = self.next_candidates_parent
            # now bubble up
            while node.parent:
                if node.value > node.parent.value:
                    break
                self._swap(node, node.parent)
            if self.next_candidates_parent.right:
                # this node is full
