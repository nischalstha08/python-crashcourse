users = ['ram', 'abram', 'hilo']
data = ['23', 'hukama']

emptylist = []

print("ram" in emptylist)

print(users[1])
print(users[-1])

print(users.index('hilo'))

print(users[0:2])
print(users[0:])

print(len(users))

users.append('Joker')
print(users)

users += ['Jason']
print(users)

users.extend(['Ronan', 'Kira'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Babina')
print(users)

users[2:2] = ['raju', 'Baby']
print(users)

users[1:3] = ['Rob', 'JPS']
print(users)

users.remove('Rob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

#del data
data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [3,45,22,42,1]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy =nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, 'kam', True])
print(mylist)

# Tuples

mytuple = tuple(('Giggity', 32, False))
anothertuple = (1,2,3)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Karma')
newtuple = tuple(newlist)
print(newtuple)
print(newlist)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)