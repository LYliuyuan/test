import time
import collections
import itertools


def maxratewithdraw(nums: list):
    if len(nums) < 2:
        return 0
    maxnet = nums[0]
    minrate = nums[0] / nums[1]
    for i in range(1, len(nums)):
        maxnet = max(nums[i], maxnet)
        minrate = min(minrate, nums[i] / maxnet)
    return 1 - minrate


def hIndex(citations) -> int:
    nlength = len(citations)
    left = 0
    right = nlength
    while left < right:
        h_idx = (left + right) // 2
        paper_cnt = 0
        for citenum in citations:
            if citenum >= h_idx:
                paper_cnt += 1
        if paper_cnt >= h_idx:
            left = h_idx
        else:
            right = h_idx - 1
    return h_idx


def subarraySum(nums, k: int) -> int:
    presum, nowsum = 0, 0
    sum_dict = {}
    cnt = 0
    for i in range(len(nums)):
        nowsum += nums[i]
        if nowsum - k in sum_dict:
            cnt += sum_dict[nowsum - k]
        if nowsum in sum_dict:
            sum_dict[nowsum] += 1
        else:
            sum_dict[nowsum] = 1
    return cnt


def numSquares(n: int) -> int:
    dq = collections.deque([n])
    cnt = 0
    cheked = set()
    while dq:
        cnt += 1
        for i in range(len(dq)):
            tempnum = dq.popleft()
            for j in range(1, int(tempnum ** 0.5) + 1):
                gap = tempnum - j ** 2
                if gap == 0:
                    return cnt
                if gap not in cheked:
                    cheked.add(gap)
                    dq.append(gap)
    return cnt


def isPalindrome(s: str) -> bool:
    nlen = len(s)
    left, right = 0, nlen - 1
    while left < right:
        while not s[left].isalpha():
            left += 1
        while not s[right].isalpha():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
    return True


# 排序算法相关：
def bubblesort(nums: list):
    neln = len(nums)
    for i in range(neln - 1, 0, -1):
        for idx in range(i):
            if nums[idx] < nums[idx + 1]:
                temp = nums[idx]
                nums[idx] = nums[idx + 1]
                nums[idx + 1] = temp
    print(nums)

def bubblesort2(nums:list):
    nlen= len(nums)
    for i in range(nlen -1):
        for j in range(nlen - 1, i,-1):
            if nums[j] >=nums[j-1]:
                temp = nums[j]
                nums[j] = nums[j-1]
                nums[j-1]=temp
    print(nums)

def choosesort(nums: list):
    nlen = len(nums)
    for i in range(nlen):
        maxidx = i
        for j in range(i + 1, nlen):
            if nums[maxidx] < nums[j]:
                maxidx = j
        nums[i], nums[maxidx] = nums[maxidx], nums[i]
    print(nums)


def quicksort(nums):
    if len(nums) >= 2:
        flgnum = nums[0]
        left = [nums[x] for x in range(1, len(nums)) if nums[x] >= flgnum]
        right = [nums[x] for x in range(1, len(nums)) if nums[x] < flgnum]
        return quicksort(left) + [flgnum] + quicksort(right)
    else:
        return nums


def partition(nums, start, end):
    l = start
    r = end
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] <= pivot:
            r -= 1
        if l < r:
            nums[l] = nums[r]
            l += 1
        while l < r and nums[l] >= pivot:
            l += 1
        if l < r:
            nums[r] = nums[l]
            r -= 1
    nums[l] = pivot
    return l


def partition2(nums, start, end):
    flg = nums[start]
    l = start
    r = end
    while l < r:
        while l < r and nums[r] <= flg:
            r -= 1
        while l < r and nums[l] >= flg:
            l += 1
        nums[r], nums[l] = nums[l], nums[r]
    nums[start] = nums[l]
    nums[l] = flg
    return l


def quiksortmain(nums, l, r):
    if l < r:
        mididx = partition2(nums, l, r)
        quiksortmain(nums, mididx + 1, r)
        quiksortmain(nums, l, mididx - 1)
    # print(nums)


def lengthOfLongestSubstring(s: str) -> int:
    nlen = len(s)
    left, right = 0, 0
    max_len_sub = 0
    while right < nlen:
        if s[right] in s[left:right]:
            left = left + s[left:right].index(s[right]) + 1
        right += 1
        max_len_sub = max(max_len_sub, right - left)
    return max_len_sub if max_len_sub != 0 else len(s)


def minSubArrayLen(target: int, nums):
    left, right = 0, 0
    minsublen = len(nums)+1
    sumnum = 0
    while right < len(nums):
        sumnum += nums[right]
        while sumnum >= target:
            minsublen = min(minsublen, right - left + 1)
            sumnum -= nums[left]
            left += 1
        right+=1
    return minsublen


if __name__ == "__main__":
    bubblesort2([2,4,6,89,3,4,89,42,99,45,8,98,34,22])
    # choosesort([2,4,6,89,3,4,89,42,99,45,8,98,34,22])
    # print(quicksort([2,4,6,89,3,4,89,42,99,45,8,98,34,22]))
    # numsl=[3,2,3,1,2,4,5,5,6]
    # startid,endid=0,len(numsl)-1
    # quiksortmain(numsl,startid,endid)
    # print(numsl)
    # print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    pass

    # s=Solution()
    # s.rotate([1,2,3,4,5],2)
