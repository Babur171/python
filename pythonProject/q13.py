def max_in_list(lst):
  max = lst[0]
  for n in lst:
    if n > max:
      max = n
  return max
print(max_in_list([-12, 3, 4, 5, 6, 7, 8, 8, 9, 10]))