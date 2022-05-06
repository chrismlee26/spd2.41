from typing import List

# 1 Given an array of 'n' nubers and a target value 't', find two numbers whose sum is 't':
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 => [3, 7] or [6, 4] or [8, 2]


def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return [numbers[left], numbers[right]]


arr = [5, 3, 6, 8, 2, 4, 7]
t = 10
print("#1 Two Sum Basic")
print("Initial Values: ", arr, "target Value: ", t)
print(twoSum(arr, t), "\n")



# 2 Two Sum II - Input Array is sorted
# Given a 1-indexed array of integers numbers that are already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length
#  numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length

def twoSum2(numbers: List[int], target: int) -> List[int]:
    # Outer Loop
    for i in range(len(numbers)):
        # Inner Loop, range of nums and stop at length of input
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target:
                    # Return index values
                    return ([i+1, j+1])


print("#2 Two Sum Sorted Ascending")
arr2 = [2, 7, 11, 15]
t2 = 9
print(twoSum2(arr2, t2), "Bad solution, repeats indexes if duplicates in input")

def twoSumSorted(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers)-1
    while left <= right:
        curr_sum = numbers[left] + numbers[right]
        if target == curr_sum:
            return [left + 1, right + 1]
        elif target > curr_sum:
            left += 1
        else:
            right -= 1
    return []

print(twoSumSorted(arr2, t2), "Better solution", "\n")

# 3 Given an array 'a' of 'n' numbers and a count 'k', find the 'k' largest values in the array 'a'.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
def largest_sum(array, count):
    sorted_arr = sorted(array)
    return sorted_arr[(count * -1):]

print("#3 Largest nums in array")
sample_array = [5, 1, 3, 6, 8, 2, 4, 7]
sample_count = 3
print(largest_sum(sample_array, sample_count), "\n")


# 4 Given two arrays 'a' and 'b' of numbers and a target value 't', find a number from each array whose sum is closest to 't'.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]
def two_array_sum(arr1, arr2, target):
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if (arr1[i] + arr2[j] == target):
                print (arr1[i], arr2[j])

print("#4 Target sum from two arrays")
a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
t = 19

two_array_sum(a, b, t)