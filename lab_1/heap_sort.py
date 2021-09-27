from timeit import default_timer as time

def swap(arr, i, j, counters):
    arr[i], arr[j] = arr[j], arr[i]
    counters[0]+=1
    return counters

def heapify(arr, n, i, order, counters):
    left = 2*i + 1
    right = 2*i + 2
    largest = i

    if order == "asc":    
        if left < n and arr[i] < arr[left]:
            largest = left
            counters[1]+=1

        if right < n and arr[largest] < arr[right]:
            largest = right
            counters[1]+=1
        
        if largest != i:
            swap(arr, i, largest, counters)                
            heapify(arr, n, largest, order, counters)
    else:
        if left < n and arr[i] > arr[left]:
            largest = left
            counters[1]+=1

        if right < n and arr[largest] > arr[right]:
            largest = right
            counters[1]+=1
        
        if largest != i:
            swap(arr, i, largest, counters)        
            heapify(arr, n, largest, order, counters)

def heap_sort(arr, order):
    n = len(arr)
    counter_swaps = 0
    counter_compares = 0
    counters = [counter_swaps, counter_compares]

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, order, counters)

    for i in range(n-1, 0, -1):
        swap(arr, 0, i, counters)   
        heapify(arr, i, 0, order, counters)
    
    return counters

if __name__ == '__main__':

    print("Welcome to Heap sort")
    print("Input elements using ',' ")
    arr = list(map(int, input().split(",")))
    print("Input asc or desc")
    order = input()

    start_time = time()
    counters = heap_sort(arr, order)
    sort_time = (float(time() - start_time))*1000
    print("Sorting time:", sort_time,"ms" )
    print("Swaps:", counters[0])
    print("Comparisons", counters[1])
    for i in range(len(arr)):
        print (arr[i], end = ' ')



