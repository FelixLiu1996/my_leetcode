class MyHashSet:

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.hash = []
    #
    # def add(self, key: int) -> None:
    #     self.hash.append(key)
    #
    # def remove(self, key: int) -> None:
    #     if key not in self.hash:
    #         return
    #     self.hash.remove(key)
    # def contains(self, key: int) -> bool:
    #     """
    #     Returns true if this set contains the specified element
    #     """
    #     if key in self.hash:
    #         return True
    #     return False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = set()

    def add(self, key: int) -> None:
        self.hash.add(key)

    def remove(self, key: int) -> None:
        if key not in self.hash:
            return
        self.hash.remove(key)
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hash:
            return True
        return False
