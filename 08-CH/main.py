def greet_user():
    """when python generates docs it looks for a string immediately
    after the function definition
    """
    text = "Hello Dave"
    print(f'well {text}')
    
    
def fav_book(fav_book):
    print(f'My favourite book is {fav_book}')
    
def get_fav_book():
    my_fave = input("Enter your favourite book\n")
    print(f'Your favourite book is {my_fave}')
    
#positional arguments and default value for pet_name
def describe_pets(animal_type,pet_name='dog'):
    """display info about pet"""
    print(f"\nI have a {animal_type}. ")
    print(f"My {animal_type}'s name is {pet_name.title()}")
    
    
def get_formatted_name(first_name,last_name,middle_name=''):
    """Return the full name neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
new_musician = get_formatted_name("john",'hooker','lee')

    
greet_user()
fav_book("Dune")
get_fav_book()

describe_pets("Dog","Cuddles")

#call using keyword arguments
describe_pets(animal_type="cat",pet_name='fluffy')
describe_pets(animal_type='elephant')
print(musician)
print(new_musician)
