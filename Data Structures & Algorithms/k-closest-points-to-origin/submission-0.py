class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max-heap de mărime k, simulat cu distanțe negative: (-dist², x, y)
        # heap[0] e mereu punctul CEL MAI ÎNDEPĂRTAT dintre cele k păstrate
        heap = []

        for x, y in points:
            d = x * x + y * y            # distanța la pătrat, fără sqrt

            if len(heap) < k:
                # încă nu avem k puncte: îl adăugăm direct
                heapq.heappush(heap, (-d, x, y))
            elif d < -heap[0][0]:
                # punctul nou e mai apropiat decât cel mai îndepărtat păstrat:
                # îl scoatem pe acela și îl punem pe cel nou, într-o operație
                heapq.heapreplace(heap, (-d, x, y))
            # altfel e mai departe decât toate cele k păstrate: îl ignorăm

        return [[x, y] for _, x, y in heap]