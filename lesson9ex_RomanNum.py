def romanToInt(s):
    total = 0
    i = 0
    my_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    if len(s) < 1 or len(s) > 15 :
        print("Invalid input!")
    while i < len(s):
        if i+1 < len(s):
                if s[i] == 'I' and s[i+1]  == 'V':
                   total += 4
                   i += 2
                   continue
                elif s[i] == 'I' and s[i+1] == 'X':
                   total += 9
                   i += 2
                   continue
                elif s[i] == 'X' and s[i+1] == 'L':
                   total += 40
                   i += 2
                   continue
                elif s[i] == 'X' and s[i+1] == 'C':
                   total += 90
                   i += 2
                   continue
                elif s[i] == 'C' and s[i+1] == 'D':
                   total += 400
                   i += 2
                   continue
                elif s[i] == 'C' and s[i+1] == 'M':
                   total += 900
                   i += 2
                   continue
        for (key,value) in my_dict.items():
            if s[i] == key:
               total = total + my_dict[key]
        i += 1
    print(total)
romanToInt('MCMXCIV')
                
                
                
    
