# a - list numbers
a = []
print (' For stop insert digits ,enter 0 or negative digit')
while True :
    x = int(input( ' Enter the number :'))
    if x == 0 or x < 0:
        print (' Goodbye')
        break
    else  :
        number = int(x)
        a.append(number)
    #else :
        #break
min_number = min(a)
max_number = max(a)
print ('Smalless :',(min_number ))
print ('Bigger :' , max_number)







