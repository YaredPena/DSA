def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1

        while j >= 0 and temp < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
            nums[j + 1] = temp 
nums = [12, 11, 13, 5, 6]
insertion_sort(nums)
print("Sorted array:", nums)
    ##pass