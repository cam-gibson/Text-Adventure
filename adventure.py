# Name: Cameron Gibson
# Date: 9/30/26
# Description:

health = 10
print(f'Health: {health}')
first_choice = str(input('Enter "left" or "right" '))

if first_choice == 'left':
    print('You have chosen to take charmander will you fight or run?')
    print(f'Health: {health}')
    second_choice = str(input('Enter "fight" or "run" '))
    
    if second_choice == 'fight':
        print('You have chosen to fight squirtle, if you want to try to catch him enter "take" if not select "leave" ')
        
        third_choice = str(input('Enter "take" or "leave" '))
        
        if third_choice == 'take':
            print(f'Health: {health}')
            print('You have won')
        
        elif third_choice == 'leave':
            health -= 10
            print(f'Health: {health}')
            print('You turned your back on squirtle and you were captured, you lost.')    
    
    elif second_choice == 'run':
        health -= 4
        print(f'Health: {health}')
        print('You have ran from squirtle, if you want to take charmander select "take" if not select "leave" ')

        third_choice = str(input('Enter "take" or "leave" '))

        if third_choice == 'take':
            print(f'Health: {health}')
            print(f'You have chosen to take charmander with you on your journey and now he can protect you, you win.')

        elif third_choice == 'leave':
            health -= 6
            print(f'Health: {health}')
            print(f'You have chosen to leave charmander and you were attacked by wild pokemon, you lose.')


elif first_choice == 'right':
    health -= 5
    print('You have chosen squirtle will you fight or run?')
    print(health)
    second_choice = str(input('Enter "fight" or "run" '))


    