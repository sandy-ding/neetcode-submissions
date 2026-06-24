class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.backtrack([], candidates, target, 0)
        return self.res

    def backtrack(self, perm: List[int], candidates: List[int], target: int, index: int):
        if target == 0:
            self.res.append(perm[:])
            return

        for i in range(index, len(candidates)):
            # if i > index and candidates[i] == candidates[i - 1]:
            #     continue
            if i == index or (i > index and candidates[i] != candidates[i - 1]):
                if candidates[i] > target:
                    break
                perm.append(candidates[i])
                self.backtrack(perm, candidates, target-candidates[i], i + 1)
                perm.pop()
