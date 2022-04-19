input_num = [2, 4, 5, 9, 1, 3, 6]

def bubble_sort(numbers):
  for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
      if numbers[j] > numbers[j+1]:
        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
  return numbers

print(bubble_sort(input_num))