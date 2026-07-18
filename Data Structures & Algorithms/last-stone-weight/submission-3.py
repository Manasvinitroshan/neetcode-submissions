class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-x for x in stones]
        heapq.heapify(heap)

        #[-2,-2,-1]
        -6,-4

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if second > first:
                heapq.heappush(heap,first-second)
            

       
        return abs(heap[0]) if heap else 0


       


                    

        