list_one = ["Mairead","David","Oisin","Saoirse"]
list_two = ["Adam","Leah","David","Mairead","Saoirse","Oisin"]
counter = 0
for i in range(0,len(list_one)):
    for j in range(0,len(list_two)):
        if list_one[i] == list_two[j]:
            counter += 1
print(counter)