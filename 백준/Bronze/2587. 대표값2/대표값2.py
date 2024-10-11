nums = []
for _ in range (5):
  num = int(input())
  nums.append(num)

nums.sort()
avg = int(sum(nums)/len(nums))
mid = nums[2]

print(avg)
print(mid)