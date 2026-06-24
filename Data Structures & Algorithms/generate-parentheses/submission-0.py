class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(left: int, arr: List[str]):
            if len(arr) == 2 * n:
                res.append("".join(arr))

            right = len(arr) - left
            if left < n:
                arr.append("(")
                backtrack(left + 1, arr)
                arr.pop()
            if left > right:
                arr.append(")")
                backtrack(left, arr)
                arr.pop()

        backtrack(0, [])
        return res
            