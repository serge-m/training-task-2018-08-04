class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.itr = comb(characters, combinationLength)
        self.elem = soft_next(self.itr)

    def next(self) -> str:
        old = self.elem
        self.elem = soft_next(self.itr)
        return old

    def hasNext(self) -> bool:
        return self.elem is not None


def comb(seq, n):
    if n == 0:
        yield ""
        return
    if len(seq) < n:
        return
    if len(seq) == n:
        yield seq
        return
    for i_start, start in enumerate(seq):
        for end in comb(seq[i_start + 1:], n - 1):
            yield start + end


def soft_next(itr):
    try:
        return next(itr)
    except StopIteration:
        return None


def test1():
    c = CombinationIterator("abc", 2)
    assert c.next() == "ab"
    assert c.hasNext() is True
    assert c.next() == "ac"
    assert c.hasNext() is True
    assert c.next() == "bc"
    assert c.hasNext() is False
