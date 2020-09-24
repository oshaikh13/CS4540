import sys

# text_input = """5 5 4
# 0 0 0 0 10
# 0 5 0 1 2
# 2 0 3 7 1
# 8 9 0 1 3
# 1 5 2 3 7
# """
input_txt = sys.stdin.read().split('\n')
# text_input = text_input.split("\n")
W, H, N = map(int, text_input[0].split(" "))
prefix = [[0 for i in range(W + 1)] for i in range(H + 1)]
scales = [list(map(int, row.split(" "))) for i, row in enumerate(text_input[1:1 + H])]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] + scales[i - 1][j - 1] - prefix[i - 1][j - 1]

def num_scales(a, b, c, d):
    return prefix[c - 1][d - 1] - prefix[a - 1][d - 1] - prefix[c - 1][b - 1] + prefix[a - 1][b - 1]

curr_max = 0
for i in range(1, H + 1):
    width = min(N // i, W)
    for a in range(1, H + 2 - i):
        for b in range(1, W + 2 - width):
            curr_max = max(curr_max, num_scales(a, b, a + i, b + width))

print(curr_max)