class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict() 
        self.visited = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.visited:
            return -1
        
        self.visited.remove(key)
        self.visited.append(key)

        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.visited:
            self.cache[key] = value
            self.visited.remove(key)
            self.visited.append(key)
        else:
            if len(self.visited) == self.capacity:
                del_key = self.visited[0]
                self.visited = self.visited[1:]
                del self.cache[del_key]

            self.visited.append(key)
            self.cache[key] = value       


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)