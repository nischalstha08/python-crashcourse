import os


# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
#print(f.read())
#print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)
    
f.close()

# try:
#     f = open("name_list.txt")
#     print(f.read())
try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist.")
finally:
    f.close()
    

#Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Nash\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()


# write - override
f = open("context.txt", "w")
f.write("I deleted all the context.")
f.close()

f = open("context.txt")
print(f.read())
f.close()


# Two ways to create a new file.

#opens a file for writing, creates the file if it doesn't exist
f = open("names_list.txt", "w")
f.close()

# Creates the specified file but returns an error if the file exists
if not os.path.exists("nash.txt"):
    f = open("nash.txt", "x")
    f.close()


# Delete  a file

# avoid  an error if it doesn't exist
if os.path.exists("nash.txt"):
    os.remove("nash.txt")
else:
    print("The file you wish to delete doesn't exist.")


with open("more_names.txt") as f:
    content = f.read()
    
with open("names.txt", "w") as f:
    f.write(content)