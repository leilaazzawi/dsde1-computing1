for i in range(1, 101):
    if (i % 3 == 0):
        if (i % 5 == 0):
            print ( str(i) + ' fizz-buzz')
        print (str(i) + ' fizz')
    if (i % 5 == 0):
        print (str(i) + ' buzz')
    
