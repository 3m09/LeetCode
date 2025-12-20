class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def boro_first(nu, lo, hi, val):
            while lo < hi:
                mid = (lo+hi) // 2
                if(nu[mid] < val):
                    lo = mid + 1
                else:
                    hi = midbes
            return lo
        lis = [nums[0]]
        for i in range(1,len(nums)):
            tail = len(lis) - 1
            if lis[tail] < nums[i]:
                lis.append(nums[i])
            else:
                idx = boro_first(lis,0,tail,nums[i])
                lis[idx] = nums[i]
        return len(lis)
        