class MyHashMap(object):

    def hash_code(self, value):
        return value%7

    def __init__(self):
        self.map = []
        self.size = 0
        self.capacity = 1024

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hash_code(value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj)
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
