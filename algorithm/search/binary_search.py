def search(nums: list, target: int) -> int:
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        
        middle = (left + right) // 2
        
        if target == nums[middle]:
            return middle
        
        elif target < nums[middle]:
            right = middle - 1
            
        else:
            left = middle + 1
            
    return -1

print(search([5], 5))
