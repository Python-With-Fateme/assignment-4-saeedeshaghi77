n=int(input('how many add number in array: '))
x=[]
for i in range (n):
    number=float(input('enter your number : '))
    x.append(number)
x.sort()
print('nozoli',x)
x.sort(reverse=True)
print('soudi',x)    