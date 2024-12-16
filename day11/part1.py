from utils.Node import Node
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, 'day11.txt')

# A -> B -> C
# A -> B1 -> B2 -> C

# B -> C
# B1 -> B2 -> C

# A -> B
# A -> B1 -> B2
def update_node(head: Node, b: Node, b1: Node, b2: Node):
    a = b.prev
    c = b.next
    
    if a is not None: #in case b is head
        a.next = b1
    else:
        head = b1
        
    b1.prev = a
    b1.next = b2
    b2.prev = b1
    b2.next = c
    
    if c is not None:# in case b is tail
        c.prev = b2
        
    return head, b2

def blink(head: Node):
    current = head
    
    while current:
        if current.data == "0": #change to 1
            current.data = "1"
        elif len(current.data) % 2 == 0: #split even nr of digits
            left_data = str(int(current.data[0:len(current.data)//2]))
            right_data = str(int(current.data[len(current.data)//2:]))
            left = Node(left_data)
            right = Node(right_data)
            head, current = update_node(head, current, left, right)
        else: #multiply by 2024
            current.data = str(int(current.data) * 2024)
        
        current = current.next
        
    return head

def main():
    with open(file_path, "r") as file:
        puzzle_input = file.read()
        
    stones = puzzle_input.split(" ")
    print(f"Initial stones: {stones}")
    head = Node.array_to_doubly_linked_list(stones)
    
    for _ in range(25):
        head = blink(head)
    
    final_stones = Node.linked_list_to_array(head)
    
    print(f"Number of stones: {len(final_stones)}")
    
if __name__ == "__main__":
    main()