"""
721. Accounts Merge
Medium

"""

from collections import defaultdict
from typing import List


class Sets:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def __repr__(self):
        return f'Sets({self.parent})'

    def join(self, a, b):
        self.parent[a] = self.get_parent(a)
        self.parent[self.parent[a]] = self.get_parent(b)

    def get_parent(self, x):
        cur = x
        while self.parent[cur] != cur:
            p = self.parent[cur]
            self.parent[cur] = self.parent[p]
            cur = p
        return cur


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_to_acc = dict()
        n = len(accounts)
        sets = Sets(n)
        for acc_id, acc in enumerate(accounts):

            for j in range(1, len(acc)):
                mail = acc[j]
                if mail in mail_to_acc:
                    sets.join(acc_id, mail_to_acc[mail])
                else:
                    mail_to_acc[mail] = acc_id
            # print(sets)
        # print(sets)
        aggregated = defaultdict(set)
        for acc_id, acc in enumerate(accounts):
            p = sets.get_parent(acc_id)
            n = acc[0]
            for j in range(1, len(acc)):
                aggregated[p].add(acc[j])
        # print(aggregated)
        return [
            [accounts[acc_id][0], *sorted(set_emails)]
            for acc_id, set_emails in aggregated.items()
        ]






