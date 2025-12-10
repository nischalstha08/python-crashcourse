# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
  
# # continue skips when value = 5 so skips 5  
# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))
    
    
# names = ["dave", "sara", "john"]
# for name in names:
#     print(name)
    
# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x  == "sara":
#         break
#     print(x)
    
# for x in names:
#     if x  == "sara":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)
    
for x in range(5,105,5):
    print(x)
else:
    print("Glad that\'s over!")
    
names = ["dave", "sara", "john"]
actions = ["codes", "eats", "sleep"]
times = ["morning", "afternoon", "evening"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
    
# for action in actions:
#     for name in names:
#         print(name + " " + action + ".")
        
for action in actions:
    for name in names:
        for time in times:
            print(name + " " + action + " in the " + time)