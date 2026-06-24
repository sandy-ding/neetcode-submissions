class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], picks: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return

        for i in range(len(nums)):
            if not picks[i]:
                picks[i] = True
                perm.append(nums[i])
                self.backtrack(perm, nums, picks)
                picks[i] = False
                perm.pop()
        


        