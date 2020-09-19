import heapq
from typing import Tuple, List


def push(
    max_heap: List[int], min_heap: List[int], val: int
) -> Tuple[List[int], List[int]]:
    if not max_heap and not min_heap:
        heapq.heappush(min_heap, val)
        return max_heap, min_heap
    if not max_heap:
        if val > min_heap[0]:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, val)
        else:
            heapq.heappush(max_heap, -val)
        return max_heap, min_heap
    if len(max_heap) == len(min_heap):
        if val < -max_heap[0]:
            heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(min_heap, val)
    elif len(max_heap) > len(min_heap):
        if val < -max_heap[0]:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(min_heap, val)
    else:
        if val > min_heap[0]:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, val)
        else:
            heapq.heappush(max_heap, -val)
    return max_heap, min_heap


def median(max_heap, min_heap) -> float:
    if len(max_heap) == len(min_heap):
        return float((-max_heap[0] + min_heap[0]) / 2)
    elif len(max_heap) > len(min_heap):
        return float(-max_heap[0])
    else:
        return float(min_heap[0])
