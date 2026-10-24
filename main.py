arr = [2,7,9,11,31]
target = 9

def sum(arr, target):
  
  seen = {}

  for i , num in enumerate(arr):
    compliment = target - num

    if compliment in seen:
      return (seen[compliment], i)

    seen[num] = i

  return []


print(sum(arr, target))
