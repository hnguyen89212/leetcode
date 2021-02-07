from typing import List

'''
Accepted 02/07/2021 12:27; runtime 32 ms, memory 14 MB.
'''


class Solution:
    # not optimal, use standalone string literal instead.
    # PUSH = "Push"
    # POP = "Pop"

    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        k = 0
        for j in range(1, n + 1):
            if (k >= len(target)):
                break
            if (target[k] == j):
                operations.append("Push")
                k += 1
            else:
                operations.append("Push")
                operations.append("Pop")
        return operations


target = [1, 3]
n = 3

ops = Solution.buildArray(None, target, n)
for each in ops:
    print(each)
