import random
ar=['apple','orange','bananna','potato']
word=list(random.choice(ar))
guess='-'*len(word)
print(guess)
ar=list(guess)
counter=0
while True:
    char=input('Enter your guess : ')
    for i in range(len(word)):
        if word[i]==char:
            ar[i]=word[i]
            break    
    else:        
        counter+=1
        print('False')    
    if counter == 5:
        print('looooseerrr ')
        break
    if ar == word:
        print('you are Winner ')
        break    
    print(''.join(ar))    

