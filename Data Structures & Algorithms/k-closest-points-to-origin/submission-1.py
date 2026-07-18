class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use maxheap as the largest number will be cut first leaving the smaller numbers

        heap = []

        for i, (x,y) in enumerate(points):
            dist = x*x + y*y
            heapq.heappush(heap,(-dist,i))
        
            if len(heap)>k:
                heapq.heappop(heap)

        
        return [points[i] for _,i in heap ]


            
            