person = "Nash"
coins = 2


print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." %(person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
print(message)

player = {'person': 'Nash', 'coins': 2}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

####################
# f-strings!!!

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*8} coins left."
print(message)

message = f"\n{person.lower()} has {2*8} coins left."
print(message)

message = f"\n{player['person']} has {2*8} coins left."
print(message)

#####################
# You can pass formatting options

num = 10
print(f"\n2.31 times {num} is {2.3 * num:.2f}\n")

for num in range(1,11):
    print(f"2.31 times {num} is {2.3 * num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 4.333 is {num / 4.333:.2%}")