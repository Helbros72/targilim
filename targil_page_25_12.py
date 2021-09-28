x = int (input( 'Enter number with two or more digits :'))
sum = 0
while x != 0 :
    sum = sum + x % 10
    x = x // 10
print ( ' Sum digits =',sum)
