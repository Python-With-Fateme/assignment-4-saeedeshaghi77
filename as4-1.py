# fact 6 = 6*5*4*3*2*1
n=int(input('how many number ? : '))
for j in range(n):
    number=int(input(f'enter your number {j+1} : '))
    sum=1
    for i in range (1,number+1):
        sum*=i
    print('fact: ', sum)    
    
