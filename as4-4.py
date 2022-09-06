import random
ar=['apple','orange','bananna','potato']
word=list(random.choice(ar))
guess='-'*len(word)
print(guess)
ar=list(guess)
counter=len(word)
while True:
    char=input('Enter your guess : ')
    for i in range(len(word)): 
        if word[i]==char:
            ar[i]=word[i]
    if char not in word:
        counter-=1 
    if counter == 0:
        print('loooossser ')
        break           
    if ar == word:
        print('you are Winner ')
        break    
    print(''.join(ar))    

