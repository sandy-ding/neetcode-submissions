class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removedIntervals = 0
        intervals.sort(key=lambda x: x[1])

        def overlap(list1: List[int], list2: List[int]) -> bool:
            return list1[0] < list2[1]

        curIndex = 0
        while curIndex < len(intervals):
            baseInterval = intervals[curIndex]
            curIndex += 1
            while(curIndex < len(intervals) and overlap(intervals[curIndex], baseInterval)):
                removedIntervals+=1
                curIndex+=1
        
        return removedIntervals