# -*- coding: utf-8 -*-
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 示例 1:
# 给定数组 nums = [1,1,2], 
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
# 你不需要考虑数组中超出新长度后面的元素。
#
# 思路：


def so(nums):
    lens = 0      # 这个变量用来存储独立元素的正确位置，也就是新数组的长度
    tmp = nums[0] # 这个变量用来存储独立元素的值

    for i in range(len(nums) - 1): # 循环到倒数第二的位置
        if tmp != nums[i+1] and tmp == nums[i]:
            nums[lens+1] = nums[i+1]
            tmp = nums[i+1]
            lens += 1
    
    return lens +1 # 此处加1是因为一开始计数的时候是从第二个元素开始的，所以要再把第一个元素也加上


# 思路2：跟 p27 思路差不多，都可以利用快慢双指针 
# 定义两个指针 fast 和 slow 分别为快指针和慢指针，快指针表示遍历数组到达的下标位置，慢指针表示下一个不同元素要填入的下标位置，初始时两个指针都指向下标 1。
# 假设数组 nums 的长度为 n。将快指针 fast 依次遍历从 1 到 n−1 的每个位置，对于每个位置，如果 nums[fast] ！= nums[fast-1]
# 说明 nums[fast] 和之前的元素都不同，因此将 nums[fast] 的值复制到 nums[slow]，然后将 slow 的值加 11，即指向下一个位置。
# 遍历结束之后，从 nums[0] 到 nums[slow−1] 的每个元素都不相同且包含原数组中的每个不同的元素，因此新的长度即为 slow，返回slow 即可

def del_num2(nums):
    if not nums:
        return 0 
    
    n = len(nums)
    slow = fast = 1
    while fast < n:
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow = slow + 1
        
        fast = fast + 1
    
    return slow 

base_num = [1,1,2]
print(del_num2(base_num))

