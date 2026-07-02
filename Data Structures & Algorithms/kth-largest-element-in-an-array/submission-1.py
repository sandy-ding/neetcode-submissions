class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for i in range(k):
            minHeap.append(nums[i])
            
        heapq.heapify(minHeap)
        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heapq.heappushpop(minHeap, nums[i])
        return minHeap[0]