class BinaryIndexedTree:
 
    def __init__(self, n):
        self.size = n
        self.arr = [0] * (n + 1)
 
    def max(self, i):
        m = 0
        while i > 0:
            m = max(m, self.arr[i])
            i -= i & -i
        return m
 
    def update(self, i, v):
        while i <= self.size:
            self.arr[i] = max(v, self.arr[i])
            i += i & -i
 
def solve():
    N = int(input())
    H = tuple(map(int, input().split()))
    A = tuple(map(int, input().split()))
 
    height_sorted = sorted([(h, i) for i, h in enumerate(H)])
 
    dp = BinaryIndexedTree(N)
    for _, i in height_sorted:
        dp.update(i + 1, dp.max(i) + A[i])
    print(dp.max(N))
 
 
solve()