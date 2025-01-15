'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.'''

def top_elements(nums: list, k: int):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in count:
                 count[num] = 1
            else:
                 count[num] += 1
                 
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

nums = [1,1,1,2,2,3]
k = 2

print(top_elements(nums, k))
