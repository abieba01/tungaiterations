def ArrayChallenge(arr):
  i=0
  j=0
  k=0

  l = len(arr)
  result = sum(arr)
  mresult = result * 2
  print (f"Product of 2 * Sum of all is {mresult}")

  while j < l:

      k=0
      #j = j+1
      while k < l:
          if j == k:

              print ("Skipped")
          else:
              product = arr[j] * arr[k]
              #print (product)
              if product > mresult:

                  result = "True"
                  return True
          k=k+1
      j=j+1


input = [2,3,5,3,3,8,9,20,19,45,2,34,3,3,12,5,12,34,2,3,23]
print(ArrayChallenge(input))
