# Name: Cameron Gibson
# Date: 9/30/26
# Description: Takes you on an adventure with a pokemon chosen at random, there are many ways the story can end you must make wise decisions to win the game.

health = 10
print(f'Health: {health}')
first_choice = str(input('Enter "left" or "right" '))
if first_choice == 'left' or first_choice == 'Left':
    print(f'Health: {health}')
    print('You have chosen to take charmander will you fight or run?')
    second_choice = input('Enter "fight" or "run" ')
    
    if second_choice == 'fight' or second_choice == 'Fight':
        health -= 2
        print(f'Health: {health}')  
        print('You have chosen to fight squirtle, if you want to try to catch him enter "take" if not select "leave" ')
        
        third_choice = str(input('Enter "take" or "leave" '))
        
        if third_choice == 'take' or third_choice == 'Take':
            print(f'Health: {health}')
            print('You have caught squirtle and now him and charmander will protect you on your journey.')
            print('=== YOU WIN ===')
        
        elif third_choice == 'leave' or third_choice == 'Leave':
            health -= 10
            print(f'Health: {health}')
            print('You turned your back on squirtle and you were captured, you lost.')
            print(f'=== GAME OVER ===')    

        else:
            print('Invalid choice.')

    elif second_choice == 'run' or second_choice == 'Run':
        health -= 6
        print(f'Health: {health}')
        print('You have ran from squirtle, will you take charmander with you or leave him behind?')
    
        third_choice = str(input('Enter "take" or "leave" '))

        if third_choice == 'take' or third_choice == 'Take':
            print(f'Health: {health}')
            print(f'You have chosen to take charmander with you on your journey and now he can protect you.')
            print('=== YOU WIN ===')
        
        elif third_choice == 'leave' or third_choice == 'Leave':
            health -= 4
            print(f'Health: {health}')
            print(f'You have chosen to leave charmander and you were attacked by wild pokemon, you lose.')
            print('=== GAME OVER ===')
        else:
            print('Invalid choice.')
    
    
    else:
        print('Invalid choice.')
    
elif first_choice == 'right' or first_choice == 'Right':
    health -= 5
    print(f'Health: {health}')
    print('You have chosen squirtle will you fight or run?')
    second_choice = str(input('Enter "fight" or "run" '))

    if second_choice == 'fight' or second_choice == 'Fight':
        print(f'Health: {health}')
        print('You have chosen to fight charmander, now you may select a random power up.')
        a = 'Extra shield'
        b = 'Water Bazooka'
        answer = str(input('Enter "a" or "b" '))
        if answer == 'a' or answer == 'A':
            health -= 3
            print(f'Health: {health}')
            print(f'Your power up was: {a}')
            print(f'Your power up unfortunately did not work')
            print(f'You now have the choice to take a health bar and fight again or leave')
            
            third_choice = str(input('Enter "take" or "leave"'))
            
            if third_choice == 'take' or third_choice == 'Take':
                health += 3
                print(f'Health: {health}')
                print('You have gained 3 health.')
                print('Will you attack or run away?')
                fourth_choice = str(input('Enter "attack" or "run" '))
                
                if fourth_choice == 'attack' or fourth_choice == 'Attack':
                    health -= 5
                    print(f'Health: {health}')
                    print(f'Squirtle still isnt good enough to beat charmander')
                    print('=== GAME OVER ===')
                
                elif fourth_choice == 'run' or fourth_choice == 'Run':
                    print(f'Health: {health}')
                    print(f'You escaped with your life')
                    print('=== YOU WIN ===')
                
                else:
                    print('Invalid choice.')

            elif third_choice == 'leave' or third_choice == 'Leave':
                health -= 2
                print(f'Health: {health}')
                print('You shouldnt have turned your back on charmander he threw a fireball at you.')
                print('=== GAME OVER ===')

            else:
                print('Invalid choice.')
        
        elif answer == 'b' or answer == 'B':
            health -= 5
            print(f'Health: {health}')
            print(f'Your power up was a {b}')
            print('Unfortunately this power up could not handle charmander.')
            print(f'=== GAME OVER ===')

        else:
            print('Invalid choice.')    

    elif second_choice == 'run' or second_choice == 'Run':
        health -= 3
        print(f'Health: {health}')
        print(f'You could not run from the wild charmander and he attacks you in the back.')
        print(f'Health critically low will you leave or take a random power up?')
        third_choice = str(input('Enter "leave" or "take"' ))
        if third_choice == 'leave' or third_choice == 'Leave':
            print(f'Health: {health}')
            print('Charmander spared you but keeps you as prisoner')
            print('=== GAME OVER ===')

        elif third_choice == 'take' or third_choice == 'Take':
            print(f'Health: {health}')
            print('You have chosen to take a random power up to fiht charmander.')
            random_power_up = int(input('Enter a number between 1 and 9 to select a random power up: '))
            if 1 <= random_power_up <= 3:
                health += 5
                print(f'Health: {health}')
                print('You have chosen an evolution bar.')
                print('Squirtle has evolved into Blastoise and you defeated charmander.')
                print('=== YOU WIN ===')

            elif 4 <= random_power_up <= 6:
                health -= 2
                print(f'Health: {health}')
                print('Your random power up was a water jetpack but it does not effect charmander.')
                print('=== GAME OVER ===')

            elif 7 <= random_power_up <= 9:
                health += 10
                print(f'Health: {health}')
                print('Your random power up was a mega evolution bar and you have evolved into mega squirtle and defeated charmander with ease.')
                print('=== YOU WIN ===')

            else:
                print('Invalid choice.')
        
        
        else:
            print('Invalid choice.')

    else:
        print('Invalid choice.')

else:
    print('Invalid choice.')

    