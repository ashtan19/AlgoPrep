'''
Question: Merge K Sorted Lists (medium)

Time Complexity: O(nlogk)
Space Complexity: O(k)

Pattern: K-Way Merge
Technique: Have a heap to keep track of the smallest node 

'''



from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__(self,other):
    return self.value < other.value


def merge_lists(lists):
  resultHead, currentHead = None, None 
  currentHead = resultHead
  minheap = []
  for list in lists:
    if list:
      heappush(minheap,list)

  while minheap: 
    smallest_list = heappop(minheap)
    if resultHead == None: 
      resultHead = currentHead = smallest_list
    else:
      currentHead.next = smallest_list
      currentHead = currentHead.next
    if smallest_list.next: 
      heappush(minheap,smallest_list.next)
  return resultHead