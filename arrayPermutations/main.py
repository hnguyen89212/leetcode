'''
procedure bt(c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        bt(s)
        s ← next(P, s)
'''

'''
startIndex = fixed = 0
i = 0, 1, 2
i = 0
  swap => [1 2 3] => [1 2 3]
  permute ([2 3])

i = 1
  swap => [1 2 3] => [2 1 3]
  permute ([1 3])

i = 2
  swap => [1 2 3] => [3 2 1]
  permute ([2 1])
'''

class Solution(object):
    def _permutationHelper(self, numbers, startIndex = 0):
      # reject
      if (startIndex >= len(numbers)): return
      if (startIndex == len(numbers) - 1): return [numbers[:]]

      result = []
      for i in range(startIndex, len(numbers)):
          # remove numbers[i] from the set of entities.
          numbers[i], numbers[startIndex] = numbers[startIndex], numbers[i]
          result += self._permutationHelper(numbers, startIndex + 1)
          numbers[startIndex], numbers[i] = numbers[i], numbers[startIndex]
      return result

    def permute(self, numbers):
        return self._permutationHelper(numbers)

class Solution2(object):
    def permute2(self, nums, values=[]):
      if not nums:
        return [values]
      result = []
      for i in range(len(nums)):
        result += self.permute2(nums[:i] + nums[i+1:], values + [nums[i]])
      return result

class Solution3(object):
    def permute2Iterative(self, nums):
      results = []
      stack = [(nums, [])]
      while len(stack):
        nums, values = stack.pop()
        if not nums:
          results += [values]
        for i in range(len(nums)):
          stack.append((nums[:i]+nums[i+1:], values+[nums[i]]))
      return results

print(Solution().permute([1, 2, 3]))
