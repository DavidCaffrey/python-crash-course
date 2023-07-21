user_01 = {"username": "Dacffee=d", "first_name": "David", "last_name": "Caffrey"}

for key, value in user_01.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

for k in user_01.keys():
    print(f"\nkey: {k}")

for v in user_01.values():
    print(f"\nvalue: {v}")
# set looks like a dictionary but does not have key value pairs
user_02_set = {"python", "java", "python", "go"}
print(user_02_set)
# pdf 142
# book 105

age = int(input("whats your age :"))
print(age < 50)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1
    
# DONT MODIFY A LIST FROM A FOR LOOP INSTEAD USE A WHILE LOOP TO DO THIS

# pdf 162
# book 124