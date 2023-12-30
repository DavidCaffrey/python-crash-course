def get_list_from_user():
    my_list = []
    while True:
        print('\nPlease tell me your name:')
        print('(enter "q" at any time to quit)')
        f_name = input('First name:')
        if f_name == 'q':
            break
        else:
            my_list.append(f_name)
        l_name = input('Last Name:')
        if l_name == 'q':
            break
        else:
            my_list.append(l_name)
        print(my_list)
        
    
get_list_from_user()