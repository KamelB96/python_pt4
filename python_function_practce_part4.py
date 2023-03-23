def max_num(a, b, c):
    return max ([a, b, c])
print(f"The largest number is {max_num(12, 7, 24)}")

def mult_list(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result

num_list = [2, 4, 6, 8, 10]
print(f"All the numbers in the list multiplied equals {mult_list(num_list)}")

def rev_string(string):
    return string[::-1]
print(rev_string("hello world"))

def num_within(num, start_num, end_num):
    return start_num <= num <= end_num
print(num_within(20, 19, 36))

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1
    #print triangle
    for row in triangle:
      print(row)

pascal(4)