class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(arr, i, n):
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
        def extract_max(arr):
            mx = arr[0]
            l_elem = arr.pop()
            if len(arr) > 0:
                arr[0] = l_elem 
            heapify(arr,0,len(arr))
            return mx
        heap = [-1] * len(nums)
        for i in range(len(nums)):
            heap[i] = nums[i]
            bubble_up(heap,i)
        k_max = -1
        for i in range(k):
            k_max = extract_max(heap)
        return k_max
        