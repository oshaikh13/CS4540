# frickin TLEs on python

import heapq

def solver(m, n, f, stations):

    dp = [[[float('inf') for _ in range(f + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
    dp[1][1][f] = 0

    heap = []
    heapq.heappush(heap, (0, (1, 1, f)))


    while len(heap) > 0:
        curr_cost, curr_state = heapq.heappop(heap)
        curr_m, curr_n, curr_f = curr_state

        if curr_m == m and curr_n == n:
            break

        if curr_cost > dp[curr_m][curr_n][curr_f]:
            continue

        for dm, dn in [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]:
            
            # new state
            new_f = curr_f
            new_m = curr_m
            new_n = curr_n
            new_cost = curr_cost

            # refuel case
            if dm == 0 and dn == 0:
                new_f += 1

                if new_f > f or (new_m, new_n) not in stations:
                    continue

                new_cost += stations[(new_m,new_n)]
     
                if new_cost >= dp[new_m][new_n][new_f]:
                    continue

                heapq.heappush(heap, (new_cost, (new_m, new_n, new_f)))
                dp[new_m][new_n][new_f] = new_cost
            else:
                new_m += dm
                new_n += dn
                new_f -= 1

                # out of bounds
                if new_m > m or new_m < 1 or new_n > n or new_n < 1 or new_f < 0:
                    continue
            
                heapq.heappush(heap, (new_cost, (new_m, new_n, new_f)))
                dp[new_m][new_n][new_f] = new_cost  

    if curr_m == m and curr_n == n:
        print("{:.2f}".format(dp[m][n][0]))
    else: print("Stranded on the shoulder")


import sys
all_in = sys.stdin.read().split('\n')

read_idx = 0
cases = int(all_in[read_idx])
read_idx += 1

for _ in range(cases):
    m, n, f, k = map(int, all_in[read_idx].split(" "))
    read_idx += 1
    stations = {}
    for _ in range(k):
        split_line = all_in[read_idx].split(" ")
        location = (int(split_line[0]), int(split_line[1]))
        cost = float(split_line[2])

        if location not in stations or stations[location] > cost:
            stations[location] = cost

        read_idx += 1
    solver(m, n, f, stations)


