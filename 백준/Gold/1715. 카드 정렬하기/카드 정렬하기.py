import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))
    
if len(heap) == 1:
    print(0)
else:
    result = 0
    while len(heap) > 1:
        card1 = heapq.heappop(heap)
        card2 = heapq.heappop(heap)
        result += card1 + card2
        heapq.heappush(heap, card1 + card2)
    print(result)