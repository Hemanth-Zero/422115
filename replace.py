import heapq

def replacement_selection(arr, m):
    runs = []
    heap = arr[:m]
    heapq.heapify(heap)
    i = m
    current_run = []
    next_heap = []

    while heap:
        smallest = heapq.heappop(heap)
        current_run.append(smallest)

        if i < len(arr):
            if arr[i] >= smallest:
                heapq.heappush(heap, arr[i])
            else:
                heapq.heappush(next_heap, arr[i])
            i += 1

        if not heap:
            runs.append(current_run)
            current_run = []
            heap = next_heap
            heapq.heapify(heap)
            next_heap = []

    return runs


arr = [20, 15, 30, 10, 25, 5, 40, 35]
runs = replacement_selection(arr, 3)

for r in runs:
    print(r)