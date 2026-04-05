from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)  # userId -> list of (time, tweetId)
        self.followMap = defaultdict(set)  # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        followees = self.followMap[userId] | {userId}  # include self

        # Push most recent tweet from each followee
        for f in followees:
            tweets = self.tweetMap[f]
            if tweets:
                time, tid = tweets[-1]
                heapq.heappush(heap, (-time, tid, f, len(tweets)-1))

        res = []
        while heap and len(res) < 10:
            negTime, tid, f, idx = heapq.heappop(heap)
            res.append(tid)
            if idx > 0:
                time2, tid2 = self.tweetMap[f][idx-1]
                heapq.heappush(heap, (-time2, tid2, f, idx-1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)