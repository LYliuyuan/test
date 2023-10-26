# This is a sample Python script.
import sys
import time

class AA():

    def test(self,l1: list):
        del (l1[0])
    def test1(self,n:int):
        n= n*10
        print(n)
        return n

def reverseStr( s: str, k: int) -> str:
    def revelist(l, start, end):
        for i in range((end - start)//2):
            tempc = l[start + i]
            l[start + i] = l[end - 1 - i]
            l[end - 1 - i] = tempc

    ls = list(s)
    nlen = len(ls)
    if nlen < k:
        revelist(ls, 0, nlen)
        return ''.join(ls)
    for idx in range(nlen):
        circle = idx // k
        if circle % 2 == 1:
            continue
        start = circle * k
        end = circle * k + k
        if idx == start:
            if end < nlen:
                revelist(ls, start, end)
            else:
                revelist(ls, start, nlen)
    return ''.join(ls)


def distinctlist(nums: list):
    # 函数内部变量不要与传入变量名相同，会引起作用域不同导致执行时变量覆盖或其他问题
    nums = list(set(nums))
    nums[0] = 'A'
    print(nums)
    print(len(nums))


def maxArea(height: list[int]) -> int:
    #盛水最多容器，贪心
    maxarea = 0
    nlength = len(height)
    if nlength == 2:
        return min(height)
    for i in range(nlength - 1):
        for span in range(nlength - 1, i, -1):
            a = span - i
            b = min(height[i], height[span])
            maxarea = max(a * b, maxarea)
    return maxarea

def threeSum(nums) :
    nlength = len(nums)
    anslist=[]
    nums.sort()
    for i in range(nlength):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l,r=i+1,nlength -1
        while l < r:
            if nums[i] + nums[l] + nums[r] ==0:
                anslist.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r] == nums[r-1]:
                    r-=1
                l += 1
                r -= 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
    return anslist
if __name__ == '__main__':
    print(threeSum([-1,-1,0,1]))
    # n=20
    # print(n)
    # print(AA().test1(n))
    # print(n)