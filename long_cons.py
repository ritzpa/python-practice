nums = [100, 4, 200, 1, 3, 2]

def long_sub(nums):
  num_set = set(nums)
  longest = 0

  for num in num_set:
    if num-1 not in num_set:

      cur_num = num
      cur_lenth =1

      while cur_num +1 in num_set:
        cur_num += 1
        cur_lenth += 1

    longest = max(cur_lenth,longest)


  return longest



print(long_sub(nums))
      