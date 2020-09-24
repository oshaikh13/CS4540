# heavily inspired by the editorial code :)

import sys
raw_input = sys.stdin.readline

N, Q = map(int, raw_input().split())
ratings = list(map(int, raw_input().split()))

max_left = [0 for i in range(N)]
max_left[0] = ratings[0]

freq_left = [0 for i in range(N)]
freq_left[0] = 1

for i in range(1, N):
    if ratings[i] > max_left[i - 1]:
        max_left[i] = ratings[i]
        freq_left[i] = 1
    elif ratings[i] == max_left[i - 1]:
        max_left[i] = max_left[i - 1]
        freq_left[i] = freq_left[i - 1] + 1
    else:
        max_left[i] = max_left[i - 1]
        freq_left[i] = freq_left[i - 1]

max_right = [0 for i in range(N)]
max_right[-1] = ratings[-1]

freq_right = [0 for i in range(N)]
freq_right[-1] = 1

for i in list(range(0, N - 1))[::-1]:
    if ratings[i] > max_right[i + 1]:
        max_right[i] = ratings[i]
        freq_right[i] = 1
    elif ratings[i] == max_left[i + 1]:
        max_right[i] = max_right[i + 1]
        freq_right[i] = freq_right[i + 1] + 1
    else:
        max_right[i] = max_right[i + 1]
        freq_right[i] = freq_right[i + 1]

max_left = [0] + max_left + [0]
max_right = [0] + max_right + [0]

freq_left = [0] + freq_left + [0]
freq_right = [0] + freq_right + [0]

for i in range(Q):
    a, b = map(int, raw_input().split())
    curr_max = max(max_left[a - 1], max_right[b + 1])
    if max_left[a - 1] == max_right[b + 1]:
        freq = freq_left[a - 1] + freq_right[b + 1]
    elif max_left[a - 1] > max_right[b + 1]:
        freq = freq_left[a - 1]
    else:
        freq = freq_right[b + 1]
    print(curr_max, freq)
