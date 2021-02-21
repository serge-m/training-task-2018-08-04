class FenwickTree:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)

    def sum(self, k: int) -> int:
        ans = 0
        while k:
            ans += self.nums[k]
            k &= k - 1
        return ans

    def add(self, k: int, x: int) -> None:
        k += 1
        while k < len(self.nums):
            self.nums[k] += x
            k += k & -k


def test_1():
    tree = FenwickTree(10)
    tree.add(1, 1)
    tree.add(5, 7)
    assert tree.sum(10) == 8
    assert tree.sum(0) == 0
    assert tree.sum(1) == 0
    assert tree.sum(2) == 1
    assert tree.sum(4) == 1
    tree.add(2, 3)
    tree.add(1, -5)
    assert tree.sum(10) == 6
    assert tree.sum(2) == 1 - 5
    assert tree.sum(3) == 1 - 5 + 3
    assert tree.sum(3) - tree.sum(2) == 3
    tree.add(2, -1)
    assert tree.sum(3) - tree.sum(2) == 2


def test_1_1():
    tree = FenwickTree(2)
    tree.add(0, 1)
    tree.add(1, 2)
    tree.add(2, 30)
    assert tree.sum(2) == 3
    assert tree.sum(1) == 1
    tree.add(0, 10)
    assert tree.sum(2) == 1+2+10
    assert tree.sum(1) == 1+10
    assert tree.sum(0) == 0


def test_2():
    k = 15
    print(k, bin(k))
    while k:
        print(k, bin(k))
        k &= k - 1


def test_3():
    k = 14
    print(k, bin(k))
    k += 1
    while k < 2000:
        print(k, bin(k))
        k += k & -k
