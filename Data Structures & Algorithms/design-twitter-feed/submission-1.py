from _heapq import heappop
class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.twitterMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitterMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        minHeap = []
        res = []
        if len(self.followMap[userId]) <= 10:
            for followeeId in self.followMap[userId]:
                if followeeId in self.twitterMap:
                    i = len(self.twitterMap[followeeId]) - 1
                    c, tid = self.twitterMap[followeeId][i]
                    heapq.heappush(minHeap, [c, tid, followeeId, i])
        else:
            maxHeap = []
            for followeeId in self.followMap[userId]:
                if followeeId in self.twitterMap:
                    i = len(self.twitterMap[followeeId]) - 1
                    c, tid = self.twitterMap[followeeId][i]
                    heapq.heappush(maxHeap, [-c, tid, followeeId, i])
                if len(maxHeap) > 10:
                    heapq.heappop(maxHeap)
            while maxHeap:
                c, tid, followeeId, i = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-c, tid, followeeId, i])
        while minHeap and len(res) < 10:
            c, tid, followeeId, i = heapq.heappop(minHeap)
            res.append(tid)
            if i - 1 >= 0:
                c, tid = self.twitterMap[followeeId][i - 1]
                heapq.heappush(minHeap, [c, tid, followeeId, i - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
