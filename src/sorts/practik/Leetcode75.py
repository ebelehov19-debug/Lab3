class Solution:
    def sortColors(self, nums: list[int]) -> None:
        a=[0]*3
        for i in nums:
            a[i]+=1
        b=[]
        j=0
        for i in range(3):
            while a[i]>0:
                nums[j]=i
                a[i]-=1
                j+=1
