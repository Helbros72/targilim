n = int (input(' Enter number :'))
while n > 10 :
    n = n // 10
    if n > 100 :
        n = n // 100
print (n)
