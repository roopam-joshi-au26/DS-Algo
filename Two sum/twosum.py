'''https://leetcode.com/problems/two-sum/'''

'''1.In this we can store each number in a dictionary with the index as a value.
2.By subtracting every number from target, we can check remaining part in dictionary if found then we can directly return 
the index of both number.
'''

def twoSum(nums,target):
    store= dict()
    for i in range (len(nums)):
        result= target-nums[i]
        if result not in store:
            store[nums[i]]=i
        else:
            return [store[result],i]


target=int(input())
nums=list(map(int,input().split()))
print(twoSum(nums,target))