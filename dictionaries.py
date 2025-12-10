# dictionaries
band ={
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals ="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# get all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a keys exists
print("guitar" in band)
print("lap" in band)

# change value in dict
band["vocals"] = "chester"
band.update({"bass": "JPJ"})

print(band)

# removing a item
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

# Delete and clear item
band["drums"] = "Bonham"
del band["drums"] 
print(band)

band2.clear()
print(band2)

del band2

# Copy a dictionary
# band2 = band #creates a refernce , refers to same place in memory
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good Copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested Dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Plant",
    "instrument": "guitar"
}
band ={
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

# Sets
nums = { 1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates in set
nums = { 1, 2, 2, 3}
print(nums)

# True is a dupe of 1, False is dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# nums = { 2, 1, 55, 3, 3, 7, 2, 1}
# print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or key

# Add a new element in a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictionaries, too

# Merge two sets to create a new set
one = {1, 2, 3}
two = ( 5, 6, 7)

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = ( 2, 3, 7)

one.intersection_update(two)
print(one)

# Keep everything except duplicates
one = {1, 2, 3}
two = ( 2, 3, 7)

one.symmetric_difference_update(two)
print(one)

