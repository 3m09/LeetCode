def findMaximizedCapital(k: int, w: int, profits, capital) -> int:
    def heapify(arr, i, n):
        if n == 0:
            return
        l_child = 2*i + 1
        r_child = 2*i + 2
        mx_idx = i
        if l_child < n and arr[l_child] > arr[mx_idx]:
            mx_idx = l_child
        if r_child < n and arr[r_child] > arr[mx_idx]:
            mx_idx = r_child
        if mx_idx == i:
            return
        arr[i], arr[mx_idx] = arr[mx_idx], arr[i]
        heapify(heap,mx_idx,n)
    def bubble_up(arr, i):
        if i <= 0:
            return
        parent_idx = ( i - 1 ) // 2
        if arr[parent_idx] < arr[i]:
            arr[parent_idx], arr[i] = arr[i], arr[parent_idx]
            bubble_up(arr,parent_idx)
    def extract_max(arr,n):
        mx = arr[0]
        l_elem = arr.pop()
        if len(arr) > 0:
            arr[0] = l_elem 
        heapify(arr,0,n-1)
        return mx
    def heapify_min(arr, i, n):
        nonlocal capital
        if n == 0:
            return
        l_child = 2*i + 1
        r_child = 2*i + 2
        mn_idx = i
        if l_child < n and capital[arr[l_child]] < capital[arr[mn_idx]]:
            mn_idx = l_child
        print('r_child:',r_child)
        print('arr[r_child]:',arr[r_child] if r_child < n else 'N/A')
        print('capital[arr[mn_idx]]:',capital[arr[mn_idx]])
        if r_child < n and capital[arr[r_child]] < capital[arr[mn_idx]]:
            mn_idx = r_child
        if mn_idx == i:
            return
        arr[i], arr[mn_idx] = arr[mn_idx], arr[i]
        heapify_min(heap,mn_idx,n)
    def bubble_up_min(arr, i):
        nonlocal capital
        if i <= 0:
            return
        parent_idx = ( i - 1 ) // 2
        if capital[arr[parent_idx]] > capital[arr[i]]:
            arr[parent_idx], arr[i] = arr[i], arr[parent_idx]
            bubble_up_min(arr, parent_idx)
    def extract_min(arr,n):
        mn = arr[0]
        l_elem = arr.pop()
        if len(arr) > 0:
            arr[0] = l_elem 
        heapify_min(arr,0,n-1)
        return mn

    mn_heap = [-1] * len(capital)
    mx_heap = [-1] * len(profits)

    for i in range(len(capital)):
        mn_heap[i] = i
        bubble_up_min(mn_heap,i)
    tmp_k = k
    tmp_w = w

    mx_heap_pos = 0

    while(tmp_k > 0):
        while(mn_heap):
            if tmp_w < capital[mn_heap[0]]:
                break
            mn_cap_idx = extract_min(mn_heap,len(mn_heap))
            mx_heap[mx_heap_pos] = profits[mn_cap_idx]
            bubble_up(mx_heap,mx_heap_pos)
            mx_heap_pos += 1
        if mx_heap_pos == 0:
            break
        p = extract_max(mx_heap,mx_heap_pos)
        tmp_w += p
        tmp_k -= 1
        mx_heap_pos -= 1
    return tmp_w

findMaximizedCapital(2,0,[1,2,3],[0,1,1])
        