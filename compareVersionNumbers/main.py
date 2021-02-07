
# def stripLeadingZeros(revision: str) -> str:
#     onlyZeros = True
#     j = 0
#     for each in revision:
#         if each != '0':
#             onlyZeros = False
#             break
#         j += 1

#     return '0' if onlyZeros else revision[j:]

'''
Accepted 02/07/2021 15:50; runtime 28 ms, memory 14.4 MB.
'''


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        result = 0
        store1 = version1.split('.')
        store2 = version2.split('.')

        length1 = len(store1)
        length2 = len(store2)
        length = length1 if length1 > length2 else length2

        for j in range(0, length):
            revision1 = '0' if j >= length1 else store1[j]
            revision2 = '0' if j >= length2 else store2[j]

            revision1 = int(revision1)
            revision2 = int(revision2)

            if revision1 > revision2:
                return 1
            elif revision1 < revision2:
                return -1
        return result
