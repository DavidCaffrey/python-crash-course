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
