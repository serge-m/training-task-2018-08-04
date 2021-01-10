"""
380. Insert Delete GetRandom O(1)
Medium

https://leetcode.com/discuss/interview-experience/1005470/Amazon-Phone-Interview-or-SDE2-or-AWS-or-Dec-2020-Reject

t=13
"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.val_to_array_index = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        pos = self.val_to_array_index.get(val)
        if pos is None:
            self.val_to_array_index[val] = len(self.array)
            self.array.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        pos = self.val_to_array_index.get(val)
        if pos is None:
            return False

        val_last = self.array[-1]
        self.array[-1], self.array[pos] = self.array[pos], self.array[-1]
        self.val_to_array_index[val_last] = pos
        del self.val_to_array_index[val]
        self.array.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)


def test_1():
    obj = RandomizedSet()
    assert obj.insert(1) is True
    assert obj.remove(2) is False
    assert obj.insert(2) is True
    assert obj.getRandom() in [1,2]
    assert obj.remove(1) is True
    assert obj.insert(2) is False
    assert obj.getRandom() == 2

