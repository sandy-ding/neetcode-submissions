class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_ = { "(": ")", "{": "}", "[": "]" }
        for ch in s:
            if ch in map_:
                stack.append(ch)
            else:
                if not stack:
                    return False
                left = stack.pop()
                if map_[left] != ch:
                    return False
        return len(stack) == 0