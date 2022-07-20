def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    index = 1
    while (index < len(nums)):
        # calculate sum on each side
        print(nums[:index])
        print(nums[(index + 1):])
        print("Left Sum: " + str(sum(nums[:index])))
        print("Right Sum: " + str(sum(nums[(index + 1):])))
        if (sum(nums[:index]) == sum(nums[(index + 1):])):
            print("Equal")
            return index
        index = index + 1
    
    # no pivot index was found
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))