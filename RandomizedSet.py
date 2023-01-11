import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.value_to_index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.value_to_index:
            return False

        self.value_to_index[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.value_to_index:
            return False

        idx = self.value_to_index[val]

        self.nums[idx] = self.nums[len(self.nums) - 1]
        self.value_to_index[self.nums[len(self.nums) - 1]] = idx

        self.nums.pop()
        del self.value_to_index[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return self.nums[random.randint(0, len(self.nums) - 1)]
