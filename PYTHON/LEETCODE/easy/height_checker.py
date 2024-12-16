'''A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].'''

def height_checker(heights: list):
    before = heights.copy()
    heights.sort()
    n = len(heights)
    count = 0

    for i in range(n):
        if heights[i] != before[i]:
            count += 1

    return count



heights = [5,1,2,3,4]
res = height_checker(heights)
print(res)