message = "hello Dave from PYTHON!I said you're 'welcome to PYTHON'"
print(message)
print(
    message.title()
)  # does not change the message variable just caps all the words in the message
print(message)
print(message.lower())  # also does not change the message variable
print(message)
message = message.lower()  # changes the message variable
print(message)

first_name = "David"  #
last_name = "Caffrey"  #
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()} and {full_name.lower()}")
new_message = f"   {full_name} is a wanker   "  #
print(new_message)
print("\tThis is a\nstring \nusing\ttabs and \n newlines   ")
new_message = new_message.rstrip()  # strips whitespace from the right side of string
new_message = new_message.lstrip()  # strips whitespace from the left side of string
print(new_message)  # could use .strip() instead to remove whitespace from both sides


netflix_url = "http://netflix.com"
netflix_url.removeprefix("http://")  # remove
print(netflix_url)
#####################################################################
# up to this point is page 61 at top of the page chrome pdf page
#####################################################################

number_large = 14_000_000_000

print(number_large)

THIS_IS_A_CONSTANT = 456
# COMMENT

my_bike_list = ["orange", "specialized", "canondale"]

print(f"{my_bike_list[1].title()}")
my_bike_list[1] = "specialized adaptation"
print(f"{my_bike_list[1].title()}")
my_bike_list.append("v bike")
print(my_bike_list)
my_bike_list.insert(0, "penny fahing")
print(my_bike_list)
# removes and deletes by index
del my_bike_list[4]
print(my_bike_list)
# pop removes for use
my_bike = my_bike_list.pop()
print(my_bike)
print(my_bike_list)
next_bike = my_bike_list.pop(1)
print(my_bike_list)
# to remove by value
my_bike_list.remove("penny fahing")
print(my_bike_list)
my_bike_list.append("v bike")
my_bike_list.append("x bike")
my_bike_list.append("w bike")
my_bike_list.append("z bike")
print(my_bike_list)
# delete by using another variable name
item_to_delete = "x bike"
my_bike_list.remove(item_to_delete)
print(my_bike_list)
my_bike_list.insert(3, "wicked bike")
print(my_bike_list)
# sort is permanently changing the list
print(my_bike_list.sort())
print(my_bike_list)
print(my_bike_list.sort(reverse=True))
print(my_bike_list)
# sorted(list) is temporary
print(sorted(my_bike_list))
print(my_bike_list)
print(my_bike_list.reverse())
print(my_bike_list)

print(len(my_bike_list))
print(my_bike_list[len(my_bike_list) - 3])

# CHAPTER 4
food = ["pizza", "orange", "apple", "banana"]

for item in food:
    print(item)

for num in range(1, 1001):
    print(num)


my_nums = list(range(10))
print(my_nums)
# third parameter denotes the step size
for num in range(1, 1001, 3):
    print(num)

squares = []
for i in range(1, 11):
    squared = i**2
    squares.append(squared)

print(squares)

# LIST COMPREHENSION

square2 = [value**3 for value in range(1, 11)]
print(square2)
print(square2[2:5])
print(square2[2:])
print(square2[:5])

# CHAPTER 4 page 100 pdf page 62 of book
