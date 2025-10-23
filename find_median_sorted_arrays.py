def find_median_sorted_arrays(list1, list2):
  list3 = sort(list1 + list2)
  print (f"Finally sorted list: {list3}")
  total_length = len(list3)
  if total_length % 2 == 1:
    median = list3[total_length // 2]
  else:
    median = (list3[total_length // 2 - 1] + list3[total_length // 2]) / 2
  return f"Median is : {median}"

find_median_sorted_arrays([1, 3], [2])
find_median_sorted_arrays([1, 3], [2, 4])
