# Copy List with Random Pointer

## Solution 1

- First loop: create a new Node and use hashmap to map the old node and the new node
  - We should first add None to None to the hashmap if the oldNode.next is None.
- Second loop: link the new node