# fact 6 = 6*5*4*3*2*1
number=int(input('enter your number : '))
sum=1
for i in range (1,number+1):
    sum*=i
print('fact: ', sum)    

