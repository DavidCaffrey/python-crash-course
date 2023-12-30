def build_person(first_name,last_name,age=None):
    """Return a dictionary of info about a person"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    print(person)
    return person

musician = build_person('jimi','hedrix',56)
print(musician)
print(musician['first'])