class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:

            if num - 1 not in numSet:
                current_length = 1

                while (num + current_length) in numSet:
                    current_length += 1
                
                longest = max(current_length, longest)
            
        return longest