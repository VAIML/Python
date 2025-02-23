def user_name_check (var) :
    while True : 
        if var == 'vimal':
            print ('enter password')
            val2 = input()
            password_check(val2)
            break
        else:
            print ('please re-enter the user name')
            var = input()
            continue
        
def password_check (val2) :
    while True :
        if val2 == 'yoyoupsc':
            print ('username and password accepted')
            break
        else :
            print ('reenter password')
            val2 = input()





while True :
    print ('enter user name')
    val1 = input()
    if val1.isalpha():
        user_name_check(val1)
        break
        
    else:
        print('please enter valid user name which is alphabetical characters')
        continue