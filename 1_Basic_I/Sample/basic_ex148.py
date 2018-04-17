'''Question: 
Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
Note: Do not use built-in functions.
'''

# Python code: 

def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))


'''Output sample: 
(75, -5)
'''