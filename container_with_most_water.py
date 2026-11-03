height = [1,8,6,2,5,4,8,3,7]

def cont_water(height):
  n = len(height)
  res = 0
  l = 0
  r = n -1

  while l < r :
    area = (r-l) * min(height[l] , height[r])

    res = max(res, area)

    if height[l] < height[r]:
      l = l + 1

    else:
      r= r -1


  return res 



print(cont_water(height))
    
    
