
# curr_rmq segtree boilerplate taken from somewhere online and modified, can't remember where exactly???

class LazySegmentTree:
 
    def __init__(self, N):
        self.index_size = 2 ** (N - 1).bit_length()
        self.data = [0] * (2 * self.index_size)
        self.lazy = [0] * (2 * self.index_size)
 
    def gindex(self, l, r):
        curr_l = l + self.index_size
        curr_r = r + self.index_size
        lm = (curr_l // (curr_l & -curr_l)) >> 1
        rm = (curr_r // (curr_r & -curr_r)) >> 1
        while curr_l < curr_r:
            if curr_r <= rm:
                yield curr_r
            if curr_l <= lm:
                yield curr_l
            curr_l >>= 1
            curr_r >>= 1
        while curr_l:
            yield curr_l
            curr_l >>= 1
 
    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i - 1]
            if not v: continue
            self.lazy[2 * i - 1] += v
            self.lazy[2 * i] += v
            self.data[2 * i - 1] += v
            self.data[2 * i] += v
            self.lazy[i - 1] = 0
 
    def update(self, l, r, x):
        curr_l = self.index_size + l
        curr_r = self.index_size + r
        while curr_l < curr_r:
            if curr_r & 1:
                curr_r -= 1
                self.lazy[curr_r - 1] += x
                self.data[curr_r - 1] += x
            if curr_l & 1:
                self.lazy[curr_l - 1] += x
                self.data[curr_l - 1] += x
                curr_l += 1
            curr_l >>= 1
            curr_r >>= 1

        for i in self.gindex(l, r):
            self.data[i - 1] = max(self.data[2 * i - 1], self.data[2 * i]) + self.lazy[i - 1]
 
    def query(self, l, r):
 
        self.propagates(*self.gindex(l, r))
        curr_l = self.index_size + l
        curr_r = self.index_size + r
 
        res = 0
        while curr_l < curr_r:
            if curr_r & 1:
                curr_r -= 1
                res = max(res, self.data[curr_r - 1])
            if curr_l & 1:
                res = max(res, self.data[curr_l - 1])
                curr_l += 1
            curr_l >>= 1
            curr_r >>= 1
        return res
 
N, M = map(int, input().split())
pairs = [[] for _ in range(N + 1)]
for _ in range(M):
    l, r, val = map(int, input().split())
    pairs[r].append((l, val))

tree = LazySegmentTree(N + 1)

for i in range(1, N + 1):
    curr_max = tree.query(0, i)
    tree.update(i, i + 1, curr_max)
    for l, val in pairs[i]: tree.update(l, i + 1, val)

print(tree.query(0, N + 1))
