# 2019.1.29

# Question: x is a perfect number if it can be written as:
# x = a^3 + b^3 = c^3 + d^3.
# x, a, b, c, d are all positive integers. (a, b) != (c, d)
# Give an integer n, find all perfect numbers between 1 and n. 1 and n inclusive.

def Solution1(n):

    ans = set()

    # find all cubic numbers
    cub_lst = []
    i = 1
    while i**3 <= n:
        cub_lst.append(i**3)
        i += 1

    # iterate through all combinations
    sum_set = set()
    N = len(cub_lst)
    for i in range(N):
        for j in range(i, N): # must include j==i, for cases such as 16 = 2^3 + 2^3
            if cub_lst[i] + cub_lst[j] <= n:
                if cub_lst[i] + cub_lst[j] in sum_set:
                    ans.add(cub_lst[i] + cub_lst[j])
                else:
                    sum_set.add(cub_lst[i] + cub_lst[j])

    return list(ans)

# Solution1: brute force solution
# time complexity: O((logn)^2), actually, O((log_3(n))^2)
# space complexity: O(logn), actually, log_3(n)