nums = [1, 2, 3, 4]

def prod_self_array(nums):
  n = len(nums)

  answer = [1]*n

  prefix = 1

  for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]


  suffix = 1

  for i in range(n-1,-1,-1):
    answer[i] *= suffix
    suffix *= nums[i]

  return answer



test = prod_self_array(nums)
print(test)