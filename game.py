"Игра 'Угадай число'"

import numpy as np
number=np.random.randint(1,101) #загадываем число
count=0 #для подсчета попыток угадывания

while True:
    count+=1
    predict_number = int(input("Guess number 1-100 "))
    
    if predict_number>number:
        print('The number must be less')
    elif predict_number<number:
        print('the number should be more')
    else:
        print(f'You have guessed the number. It is {number}, you used {count} tries')
        break