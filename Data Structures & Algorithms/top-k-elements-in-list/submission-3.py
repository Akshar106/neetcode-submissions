class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        
        for key, values in count.items():
            freq[values].append(key)

        result = []
        for res in range(len(freq) - 1, 0, -1):
            for num in freq[res]:
                result.append(num)

                if len(result) == k:
                    return result


        

        