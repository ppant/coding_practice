# list comprehension
# Example 1: Generating Squares and Cubes
squares = []
cubes = []
# through for loop
for x in range(10):
    squares.append(x**2)
    cubes.append(x**3)
print('loop: Squares:',squares)
print('loop: Cubes:',cubes)

# through list comprehension
squares_lc = [x**2 for x in range(10)]
cubes_lc = [x**3 for x in range(10)]
print('list comp: Squares:',squares_lc)
print('list comp: Cubes:',cubes_lc)

# Example 2: Based on a list of fruits make a new list, containing only the 
# fruits with the letter "a" in the name
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# through list comprehension
newlist_lc = [x for x in fruits if "a" in x]
print(newlist_lc)

# Generate a matrix using two for loop
matrix = [] 
for i in range(3): 
	# Append an empty sublist inside the list 
	matrix.append([]) 
	for j in range(5): 
		matrix[i].append(j) 
print(matrix) 

# Generate a matrix using list comprehension - Nested lists
matrix = [[j for j in range(5)] for i in range(3)] 
print(matrix)

# benchmarking: looping and list comprehension
# Import required module 
# Import required module 
import time 
# define function to implement for loop 
def for_loop(n): 
	result = [] 
	for i in range(n): 
		result.append(i**2) 
	return result 
# define function to implement list comprehension 
def list_comprehension(n): 
	return [i**2 for i in range(n)] 
# Driver Code 
# Calculate time taken by for_loop() 
begin = time.time() 
for_loop(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for_loop:', round(end-begin, 2)) 

# Calculate time takens by list_comprehension() 
begin = time.time() 
list_comprehension(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for list_comprehension:', round(end-begin, 2)) 

# basic lambda 
x = lambda a : a + 10
print("output using lambda:", x(6))
# Using lambda and list comprehesion
# for loop to print table of 10 
numbers = [] 
for i in range(1, 6): 
	numbers.append(i*10) 
print(numbers) 

# Using list comprehension
numbers = [i*10 for i in range(1,6)]
print(numbers)

# Using lambda and list comprehension to print table of 10 
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)])) 
print(numbers) 

# Nested IF with List Comprehension
lis = [num for num in range(100) 
	if num % 5 == 0 if num % 10 == 0] 
print(lis)

# Toggle the case of each character in a String
# Initializing string 
string = 'Geeks4Geeks'
# Toggle case of each character 
List = list(map(lambda i: chr(ord(i) ^ 32), string)) 
# Display list 
print(List) 

# Reverse each string in a Tuple
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')] 
# Display list 
print(List) 

# few examples of using list, map, filter and lambda
nums = [1, 2, 3, 4, 5]
map_out = map(lambda n: 2 * n, nums)  # print fails, so list() below
print(map_out)
lst1 = list(map(lambda n: 2 * n, nums))  # e.g. double each n
print(lst1)
lst2 = list(map(lambda n: n * -1, nums))
print(lst2)
lst3 = list(map(lambda n: 2 ** n, nums))
print(lst3)
strs = ['Summer', 'is', 'coming']
str_out = list(map(lambda s: s.upper() + '!', strs))
print(str_out)

# filter() function takes a function and a list, and returns a 
# subsetted list of the elements where the function returns true
strs = ['apple', 'and', 'a', 'donut']
lst4 = list(filter(lambda s: len(s) > 3, strs))
print(lst4)
nums_in = [5, 3, 6, 1, 7, 2]
lst4_out = list(filter(lambda n: n % 2 == 1, nums_in))
print(lst4_out)

# Append an Item to Lists Within A List Using or Operator
#list containing lists 
squares = [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]] 

#use list comprehension to append an item 
squares = [x.append('20') or x for x in squares] 

#print updated list 
print(squares)
