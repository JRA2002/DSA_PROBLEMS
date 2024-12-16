'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.'''

def max_area(height: list):
    max_area = 0
    i = 0
    j = len(height) - 1

    while i < j:
        max_area = max(max_area,min(height[i],height[j])*(j-i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

height = [1,1]

res = max_area(height)
print(res)
 