from functools import reduce 

#Problem 1: Sum of Digits
#Objective: compute the sum of the digits of a given number.
num = 4203
digits = [int(d) for d in str(num)]
f = lambda x,y: x + y
sum_digits = reduce(f,digits)
print('Problem 1:', sum_digits)

#Problem 2: Custom Sort Order
lst = ['cat', 'kitten', 'kitty','meow']
list_sorted = sorted(lst, key=lambda lst: len(lst))
print('Problem 2:' , list_sorted)

#Problem 3: Find Maximum
numbers = [42, 29, 12, 48, 56]
max_solution = lambda x,y: x if x > y else y
maximum = reduce(max_solution, numbers)
print('Problem 3:', maximum)

#Problem 4: Intersection of Two Lists
lst_1 = [1,2,3,4,5]
lst_2 = [2,4,6,8]
intersection = list(filter(lambda x: x in lst_1, lst_2))
print('Problem 4:', intersection)

#Problem 5: Exponential Mapping
list_of_numbers = [4,5,6]
n = 2
raised = list(map(lambda x: x ** n, list_of_numbers))
print('Problem 5:', raised)

