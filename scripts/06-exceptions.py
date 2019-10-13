''' Exceptions '''

t = int(input())

for _ in range(t):
    req = input().split()
    

    try:
        a = int(req[0])

        try:
            b = int(req[1])

            if b == 0:
                print('Error Code: integer division or modulo by zero')
            else: 
                print(a // b)
        
        except:
            print("Error Code: invalid literal for int() with base 10: '%s'" % req[1])
        
        
    except:
        print("Error Code: invalid literal for int() with base 10: '%s'" % req[0])

    

