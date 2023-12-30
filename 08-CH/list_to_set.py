def make_set_from_list(names):
    my_set = set()
    for name in names:
        my_set.add(name.title())
    print(my_set)
    
    for item in my_set:
        print(f"hello {item}")

names_list = ['david','mairead','oisin','saoirse','david']  
make_set_from_list(names_list)