'''Given an arr[] containing n integers and a positive integer k. The problem is to find the longest 
subarray’s length with the sum of the elements divisible by the given value k.'''

def longestSubarrWthSumDivByK(arr, n, k):

	# unordered map 'um' implemented
	# as hash table
	um = {}

	# 'mod_arr[i]' stores (sum[0..i] % k)
	mod_arr = [0 for i in range(n)]
	max_len = 0
	curr_sum = 0

	# Traverse arr[] and build up
	# the array 'mod_arr[]'
	for i in range(n):
		curr_sum += arr[i]

		# As the sum can be negative,
		# taking modulo twice
		mod_arr[i] = ((curr_sum % k) + k) % k

		# If true then sum(0..i) is
		# divisible by k
		if (mod_arr[i] == 0):

			# Update 'max_len'
			max_len = i + 1
		
        # If value 'mod_arr[i]' not present in
		# 'um' then store it in 'um' with index
		# of its first occurrence
		elif (mod_arr[i] not in um):
			um[mod_arr[i]] = i
            
		else:
			# If true, then update 'max_len'
			if (max_len < (i - um[mod_arr[i]])):
				max_len = i - um[mod_arr[i]]

	
	# Return the required length of longest subarray
	# with sum divisible by 'k'
	return max_len, um


# Driver Code
if __name__ == '__main__':

	arr = [3, 3, 1, 4, 3, 5]
	n = len(arr)
	k = 3

	print("Length =",
		longestSubarrWthSumDivByK(arr, n, k))

