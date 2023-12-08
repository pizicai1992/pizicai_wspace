# -*- coding: utf-8 -*- 
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1 


# 思路：
# 我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。
# 比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
# 我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：
# 在尽可能靠右的低位进行交换，需要从后向前查找
# 将一个 尽可能小的「大数」 与前面的「小数」交换。比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
# 将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。以 123465 为例：首先按照上一步，交换 5 和 4，
# 得到 123564；然后需要将 5 之后的数重置为升序，得到 123546。显然 123546 比 123564 更小，123546 就是 123465 的下一个排列

def solution(target_array):
    n = len(target_array)
    if n<2: return target_array
    i = n-1
    while i > 0 and target_array[i-1] >= target_array[i]: # 此处是找到从后往前的第一个“升序对”，确定 i 的值
        i -= 1
    if i == 0:
        return target_array.reverse()
    else:
        j = n-1 # j 是 右边大于array[i-1]的第一个数的下标
        while j > i-1 and target_array[j] <= target_array[i-1]:
            j -= 1
        target_array[i-1], target_array[j] = target_array[j], target_array[i-1] # 这一步就是交换
        for k in range((n-i) // 2):
                target_array[i+k], target_array[n-1-k] = target_array[n-1-k], target_array[i+k]
        return target_array


arr = [1, 1, 5]
print (solution(arr))