def personal_info(b, f, s):
    birth_year= b
    first_name = f
    sur = s
    current_year= 2020
    age= current_year - birth_year
    initials = first_name[0] + sur[0]
    print('your initials are ' +initials+ ' you are' +str(age)+ ' years old')


    
