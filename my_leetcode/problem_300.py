# -*- coding: utf-8 -*-
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 示例:
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

# 参考官方的动态规划题解
# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
# 首先有一个数组dp[] 来存储每一次循环时，以i结尾的子串的最长升序子序列的长度，将这个值存储在dp[i] 中；
# 初始化时，将dp初始成长度等于原始数组的以1填充的数据，代表的是极端情况下，原始数组中的最长子序列都是单个元素（如果原始数组就是一个降序数组，此时是极端情况）
# 内循环每次判断逻辑是：第一次，如果当前元素i比他之前的某个元素j大，那么此时dp[i]应该是2，即dp[j]+1，说明截至到i，至少能判断出有两个元素能组成升序子序列了
# 继续内循环，如果还有元素满足上述条件，说明这个元素也可以和当前元素组成升序子序列，此时dp[i] 应该是本次循环时
# 继续

def solution(seq):
    if not seq:
        return 0 
    
    dp = [1] * len(seq) # 定义一个dp数组，默认是1，dp[i] 所有元素置 1，含义是每个元素都至少可以单独成为子序列，此时长度都为 1
    for i in range(len(seq)):
    # 外循环遍历每一个元素    
        for j in range(i):
        # 内循环遍历从头当前元素的前一个元素    
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j]+1)    
    return max(dp)

testSeq = [10,9,2,5,3,7,101,18]
print (solution(testSeq))