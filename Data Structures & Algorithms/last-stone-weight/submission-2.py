class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]

        heapq.heapify(heap)

        while len(heap) >= 2:
            n1 = -heapq.heappop(heap)
            n2 = -heapq.heappop(heap)
            
            if n1 != n2:
                heapq.heappush(heap, -(n1 - n2))
            
        return -heap[0] if heap else 0