# # recursion
def add_one(num):
    if (num >= 9):
        return num + 1
    
    total = num + 1
    print(total)
    
    return add_one(total)

mynewtotal = add_one(0)
print(mynewtotal)

# # using a while loop
# def plus_one(num):
#     while num < 9:
#         num = num + 1
#         print(num)
        
#     return num + 1

# my_new_total = plus_one(0)

# # using for loop
# def plus_one(num):
#     for _ in range(9 - num):
#         num = num + 1
#         print(num)
        
#     return num + 1

# my_new_total = plus_one(0)