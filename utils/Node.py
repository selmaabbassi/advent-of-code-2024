from __future__ import annotations

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        self.prev: Node = None
        
    def array_to_doubly_linked_list(arr):
        head = Node(arr[0])
        current = head
        
        for val in arr[1:]:
            new_node = Node(val)
            current.next = new_node
            new_node.prev = current
            current = new_node
        
        return head
    
    def linked_list_to_array(head):
        arr = []
        
        current = head
        
        while current:
            arr.append(current.data)
            current = current.next
            
        return arr    