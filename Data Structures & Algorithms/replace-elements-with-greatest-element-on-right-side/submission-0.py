class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        ans = []
        for i in range(0, len(arr)-1):
            ans = arr[i+1:]
            maxi = max(ans)
            arr[i] = maxi

        return arr[:-1] + [-1]