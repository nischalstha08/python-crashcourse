squared = lambda num : num * num


print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(13))

sum_total = lambda a, b : a + b

print(sum_total(3, 6))

#####################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

######################

numbers = [3 , 5, 6, 88, 12, 21]

squared_Nums = map(lambda num : num * num, numbers)

print(list(squared_Nums))

#########################


odd_Nums = filter(lambda num : num % 2 != 0, numbers)

print(list(odd_Nums))

##########################
from functools import reduce


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))




names = ['Nash', 'Ram', 'Rita Kumari']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)