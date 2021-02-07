"""
1146. Snapshot Array
Medium

"""


class SnapshotArray:

    def __init__(self, length: int):
        self.len = length
        self.cur_id = 0
        self.versions = {
        }
        self.cur = {}

    def set(self, index: int, val: int) -> None:
        self.cur[index] = val

    def snap(self) -> int:
        self.versions[self.cur_id] = self.cur.copy()
        self.cur_id += 1
        return self.cur_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # print(self.versions)
        return self.versions[snap_id].get(index, 0)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
