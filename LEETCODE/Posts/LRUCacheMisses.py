"""
Leetcode: Amazon OA 2020 LRU Cache Misses

Attempts: 1
Completed: N and did not get idea
Acheived Ideal:
Under 30 Mins: 

Time Complexity:
Space Complexity:

Pattern: Use hashtable and doublylinkedList (Traditional) or use an OrderedDict
Technique: create a class extending the OrderedDict and keep track of misses

Problems Encountered:
Other Solutions:

"""


from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        self.misses = 0
        self.n = 0

    def hit(self, key):
        if key in self:
            self.move_to_end(key)
        else:
            self.misses += 1
            self[key] = None
            self.n += 1
        if self.n > self.capacity:
            self.popitem(last=False)
            self.n -= 1


class Solution:
    def lruCacheMisses(self, num, pages, maxCacheSize):
        lru_cache = LRUCache(maxCacheSize)
        for page in pages:
            lru_cache.hit(page)
        return lru_cache.misses
