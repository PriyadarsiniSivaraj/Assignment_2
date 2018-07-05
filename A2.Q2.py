for i in range(1,10):
    if i<= 5:
        k = i
        for j in range(k):
            print("*",end='')
        print('\r')
    else:
        k = 10
        for j in range(k-i):
                print("*",end='')
        print('\r')
